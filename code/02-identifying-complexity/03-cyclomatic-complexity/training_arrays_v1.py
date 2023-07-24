# This file contains the `model_iteration` function from the 
# `python/keras/engine/training_arrays_v1.py` file in the TensorFlow project. 
# It was retrieved from
# https://github.com/tensorflow/tensorflow/blob/7ce32a1a15c826c581ac7cad606054b7ba2fa825/tensorflow/python/keras/engine/training_arrays_v1.py
# on July 23, 2023.

# The comment header which included the file's license was been moved to the
# bottom of this file to improve readability.

# All comments from the the `model_iteration` function have been removed, and
# new comments have been added documenting the cyclomatic complexity of the
# function.

def model_iteration(model,
                    inputs,
                    targets=None,
                    sample_weights=None,
                    batch_size=None,
                    epochs=1,
                    verbose=1,
                    callbacks=None,
                    val_inputs=None,
                    val_targets=None,
                    val_sample_weights=None,
                    shuffle=True,
                    initial_epoch=0,
                    steps_per_epoch=None,
                    validation_steps=None,
                    validation_freq=1,
                    mode=ModeKeys.TRAIN,
                    validation_in_fit=False,
                    prepared_feed_values_from_dataset=False,
                    steps_name='steps',
                    **kwargs):
  
  # Cyclomatic complexity starts out at 1

  # Incremented to 2 because of the if statement
  if 'steps' in kwargs:
    steps_per_epoch = kwargs.pop('steps')
  
  # Incremented to 3 because of the if statement
  if kwargs:
    raise TypeError('Unknown arguments: %s' % (kwargs,))

  reset_dataset_after_each_epoch = False
  input_iterator = None
  is_dataset = isinstance(inputs,
                          (data_types.DatasetV1, data_types.DatasetV2))
  
  # Incremented to 4 because of the if statement
  if is_dataset:
    # Incremented to 5 because of the if statement
    if steps_per_epoch is None:
      reset_dataset_after_each_epoch = True
      steps_per_epoch = training_utils_v1.infer_steps_for_dataset(
          model, inputs, steps_per_epoch, epochs=epochs, steps_name=steps_name)
    input_iterator = _get_iterator(inputs, model._distribution_strategy)

  # Incremented to 6 because of the if statement
  if model._distribution_strategy:
    scope = distributed_training_utils_v1.distributed_scope(
        strategy=model._distribution_strategy,
        # Incremented to 7 because of the if statement
        learning_phase=(1 if mode == ModeKeys.TRAIN else 0))
    scope.__enter__()

  # Incremented to 7 because of the `or` boolean operator
  use_steps = is_dataset or steps_per_epoch is not None
  # Incremented to 8 because of the `is` boolean operator 
  do_validation = val_inputs is not None

  # Incremented to 9 because of the `or` boolean operator
  inputs = input_iterator or inputs

  # Incremented to 10 because of the if statement
  # Incremented to 11 because of the use of the `and` boolean operator
  if validation_in_fit and prepared_feed_values_from_dataset:
    ins = inputs
  else:
    ins = _prepare_feed_values(model, inputs, targets, sample_weights, mode)

  # Incremented to 12 because of the if statement
  if not is_dataset:
    num_samples_or_steps = _get_num_samples_or_steps(ins, batch_size,
                                                     steps_per_epoch)
  else:
    num_samples_or_steps = steps_per_epoch

  _update_sample_weight_mode(model, mode, ins)

  f = _make_execution_function(model, mode)

  val_iterator = None

  # Incremented to 13 because of the if statement
  if isinstance(val_inputs, (data_types.DatasetV1, data_types.DatasetV2)):
    # Incremented to 14 because of the if statement
    if validation_steps is None:
      validation_steps = training_utils_v1.infer_steps_for_dataset(
          model,
          val_inputs,
          validation_steps,
          epochs=epochs,
          steps_name='validation_steps')
    val_iterator = _get_iterator(val_inputs, model._distribution_strategy)
    val_inputs = _prepare_feed_values(
        model, val_iterator, val_targets, val_sample_weights, ModeKeys.TEST)

    val_samples_or_steps = validation_steps
  else:
    # Increments to 15 because of the use of the `and` boolean operator
    val_samples_or_steps = val_inputs and nest.flatten(
        # Increments to 16 because of the use of the `or` boolean operator
        val_inputs)[0].shape[0] or None

  # Increments to 17 because of the if statement
  # Increments to 18 because of the use of the `and` boolean operator
  if mode == ModeKeys.TRAIN and verbose:
    _print_train_info(num_samples_or_steps, val_samples_or_steps, is_dataset)

  # Increments to 19 because of the if statement
  count_mode = 'steps' if use_steps else 'samples'
  callbacks = cbks.configure_callbacks(
      callbacks,
      model,
      do_validation=do_validation,
      batch_size=batch_size,
      epochs=epochs,
      steps_per_epoch=steps_per_epoch,
      samples=num_samples_or_steps,
      count_mode=count_mode,
      verbose=verbose,
      mode=mode)

  # Increments to 20 because of the if statement
  # Increments to 21 because of the use of the `and` boolean operator
  if issparse is not None and not use_steps:
    indices_for_conversion_to_dense = []
    feed = _get_model_feed(model, mode)
    # Increments to 22 because of the condition in the for loop
    for i, (input_data, feed_tensor) in enumerate(zip(ins, feed)):
      # Increments to 23 because of the if statement
      # Increments to 24 because of the use of the `and` boolean operator
      if issparse(input_data) and not backend.is_sparse(feed_tensor):
        indices_for_conversion_to_dense.append(i)

  # Increments to 25 because of the if statement 
  if mode == ModeKeys.PREDICT:
    aggregator = training_utils_v1.OutputsAggregator(
        use_steps,
        # Increments to 26 because of the `if` statement
        num_samples=None if steps_per_epoch else num_samples_or_steps,
        steps=steps_per_epoch)
  else:
    aggregator = training_utils_v1.MetricsAggregator(
        use_steps,
        # Increments to 27 because of the `if` statement
        num_samples=None if steps_per_epoch else num_samples_or_steps,
        steps=steps_per_epoch)

  # Increments to 28 because of the `if` statement
  if model._compile_distribution:
    distributed_training_utils_v1._copy_weights_to_distributed_model(
        model, mode)

  callbacks.model.stop_training = False
  callbacks._call_begin_hook(mode)

  initial_epoch = model._maybe_load_initial_epoch_from_ckpt(initial_epoch, mode)

  # Increments to 29 because of the `if` statement
  for epoch in range(initial_epoch, epochs):
    # Increments to 30 because of the `if` statement
    if callbacks.model.stop_training:
      break

    epoch_logs = {}
    # Increments to 31 because of the `if` statement
    if mode != ModeKeys.PREDICT:
      model.reset_metrics()
    # Increments to 32 because of the `if` statement
    if mode == ModeKeys.TRAIN:
      callbacks.on_epoch_begin(epoch, epoch_logs)

    # Increments to 33 because of the `if` statement
    if use_steps:
      # Increments to 34 because of the `if` statement
      if steps_per_epoch is None:
        target_steps = np.inf
      else:
        target_steps = steps_per_epoch

      step = 0
      # Increments to 35 because of the condition in the `while` statement
      while step < target_steps:
        batch_logs = {'batch': step, 'size': 1}
        callbacks._call_batch_hook(mode, 'begin', step, batch_logs)

        try:
          # Increments to 36 because of the `if` statement
          # Increments to 37 because of the use of the `or` boolean operator
          # Increments to 38 because of the use of the `and` boolean operator
          if not callable(ins) or (model._distribution_strategy and
                                   not distributed_training_utils_v1
                                   .is_distributing_by_cloning(model)):
            actual_inputs = ins
          else:
            actual_inputs = ins()
          batch_outs = f(actual_inputs)
        except errors.OutOfRangeError:
          # Increments to the 39 because of the `if` statement
          if is_dataset:
            # Increments to 40 because of the `if` statement
            if steps_per_epoch:
              callbacks.model.stop_training = True
              logging.warning(
                  'Your dataset ran out of data; interrupting training. '
                  'Make sure that your dataset can generate at least '
                  '`%s * epochs` batches (in this case, %d batches). '
                  'You may need to use the repeat() function when '
                  'building your dataset.'
                  % (steps_name, steps_per_epoch * epochs))
            # Increments to 41 because of the `elif` statement
            elif step > 0:
              steps_per_epoch = step
              aggregator.steps = steps_per_epoch
          else:
            callbacks.model.stop_training = True
            logging.warning(
                'Your dataset iterator ran out of data; '
                'interrupting training. Make sure that your iterator '
                'can generate at least `%s * epochs` '
                'batches (in this case, %d batches). You may need to'
                'use the repeat() function when building your '
                'dataset.' % (steps_name, steps_per_epoch * epochs))
          break

        # Increments to 42 because of the `if` statement
        if not isinstance(batch_outs, list):
          batch_outs = [batch_outs]

        # Increments to 43 because of the `if` statement
        if model._distribution_strategy:
          batch_outs = (
              distributed_training_utils_v1._per_replica_aggregate_batch(
                  model._distribution_strategy, batch_outs, model, mode))

        # Increments to 44 because of the `if` statement
        if step == 0:
          aggregator.create(batch_outs)
        aggregator.aggregate(batch_outs)

        batch_logs = cbks.make_logs(model, batch_logs, batch_outs, mode)
        callbacks._call_batch_hook(mode, 'end', step, batch_logs)
        step += 1

        # Increments to 45 because of the `if` statement
        if callbacks.model.stop_training:
          break
    else:
      index_array = np.arange(num_samples_or_steps)
      # Increments to 46 because of the `if` statement
      if shuffle == 'batch':
        index_array = training_utils_v1.batch_shuffle(index_array, batch_size)
      elif shuffle:
        np.random.shuffle(index_array)
      batches = make_batches(num_samples_or_steps, batch_size)
      # Increments to 47 because of the condition in the `for` loop
      for batch_index, (batch_start, batch_end) in enumerate(batches):
        batch_ids = index_array[batch_start:batch_end]

        # Increments to 48 because of the `if` statement
        if len(batches) == 1:
          ins_batch = ins
        else:
          try:
            # Increments to 49 because of the `if` statement
            # Increments to 50 because of the use of the `and` boolean operator
            if ins and isinstance(ins[-1], int):

              ins_batch = slice_arrays(ins[:-1], batch_ids) + [ins[-1]]
            else:
              ins_batch = slice_arrays(ins, batch_ids)
          except TypeError:
            raise TypeError('TypeError while preparing batch. '
                            'If using HDF5 input data, '
                            'pass shuffle="batch".')

        # Increments to 51 because of the `if` statement
        if issparse is not None:
          # Increments to 52 because of the condition in the `for` loop
          for i in indices_for_conversion_to_dense:
            ins_batch[i] = ins_batch[i].toarray()

        batch_logs = {'batch': batch_index, 'size': len(batch_ids)}
        callbacks._call_batch_hook(mode, 'begin', batch_index, batch_logs)

        batch_outs = f(ins_batch)
        # Increments to 53 because of the `if` statement
        if not isinstance(batch_outs, list):
          batch_outs = [batch_outs]

        # Increments to 54 because of the `if` statement
        if batch_index == 0:
          aggregator.create(batch_outs)
        aggregator.aggregate(batch_outs, batch_start, batch_end)

        batch_logs = cbks.make_logs(model, batch_logs, batch_outs, mode)
        callbacks._call_batch_hook(mode, 'end', batch_index, batch_logs)

        # Increments to 56 because of the `if` statement
        if callbacks.model.stop_training:
          break

    aggregator.finalize()
    results = aggregator.results
    epoch_logs = cbks.make_logs(model, epoch_logs, results, mode)
    # Increments to 57 because of the `if` statement
    if len(results) == 1:
      results = results[0]

    # Increments to 58 because of the `if` statement
    # Increments to 59 because of the first use of the `and` boolean operator
    # Increments to 60 because of the second use of the `and` boolean operator
    if (do_validation and
        training_utils_v1.should_run_validation(validation_freq, epoch) and
        not callbacks.model.stop_training):

      # Increments to 61 because of the `if` statement
      if model._compile_distribution:
        distributed_training_utils_v1._copy_weights_to_original_model(
            model, ModeKeys.TRAIN)

      val_results = model_iteration(
          model,
          val_inputs,
          targets=val_targets,
          sample_weights=val_sample_weights,
          batch_size=batch_size,
          steps_per_epoch=validation_steps,
          callbacks=callbacks,
          verbose=0,
          mode=ModeKeys.TEST,
          validation_in_fit=True,
          # Increments to 62 because of the use of the `is` boolean operator
          prepared_feed_values_from_dataset=(val_iterator is not None),
          steps_name='validation_steps')
      # Increments to 63 because of the `if` statement
      if not isinstance(val_results, list):
        val_results = [val_results]
      epoch_logs = cbks.make_logs(
          model, epoch_logs, val_results, mode, prefix='val_')
      # Increments to 64 because of the `if` statement
      # Inrcements to 65 because of the use of the `and` boolean operator
      if val_iterator and epoch < epochs - 1:
        _reinitialize_iterator(val_iterator, model._distribution_strategy)

    # Increments to 66 because of the `if` statement
    if mode == ModeKeys.TRAIN:
      callbacks.on_epoch_end(epoch, epoch_logs)

    # Increments to 67 because of the `if` statement
    # Increments to 68 because of the use of the `and` boolean operator 
    if reset_dataset_after_each_epoch and epoch < epochs - 1:
      _reinitialize_iterator(input_iterator, model._distribution_strategy)

  model._successful_loop_finish = True
  callbacks._call_end_hook(mode)

  # Increments to 69 because of the `if` statement
  if model._distribution_strategy:
    # Increments to 70 because of the `if` statement
    if model._compile_distribution:
      distributed_training_utils_v1._copy_weights_to_original_model(model, mode)
    scope.__exit__(None, None, None)

  # Increments to 71 because of the `if` statement
  if mode == ModeKeys.TRAIN:
    # Increments to 72 because of the "extra" `return` statement
    return model.history
  # Does not increment, because it is not a new branch
  return results

  # Total function cyclomatic complexity is 72
  
# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
