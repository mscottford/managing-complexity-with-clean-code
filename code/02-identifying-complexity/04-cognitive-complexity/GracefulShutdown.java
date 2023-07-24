/*
 * This file contains the `shutdownGracefully` method within the 
 * `GracefulShutdown` class. It is included here to demonstrate how to
 * calculate the cognitive complexity of a method.
 * 
 * Comments have been added to the `shutdownGracefully` method to illustrate
 * the calculation of cognitive complexity.
 * 
 * The contents of this file were copied from the `spring-boot` project.
 * It was retrieved from https://github.com/spring-projects/spring-boot/blob/07a7ff473b6e97db6f00eb62f4f8beb2fb8da73b/spring-boot-project/spring-boot/src/main/java/org/springframework/boot/web/embedded/tomcat/GracefulShutdown.java
 * on July 23, 2023.
 * 
 * The file's original comment header has been moved to the bottom of this file.
 * It includes the license that this file is released under.
 */

package org.springframework.boot.web.embedded.tomcat;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.apache.catalina.Container;
import org.apache.catalina.Service;
import org.apache.catalina.connector.Connector;
import org.apache.catalina.core.StandardContext;
import org.apache.catalina.core.StandardWrapper;
import org.apache.catalina.startup.Tomcat;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import org.springframework.boot.web.server.GracefulShutdownCallback;
import org.springframework.boot.web.server.GracefulShutdownResult;

/**
 * Handles Tomcat graceful shutdown.
 *
 * @author Andy Wilkinson
 */
final class GracefulShutdown {

	private static final Log logger = LogFactory.getLog(GracefulShutdown.class);

	private final Tomcat tomcat;

	private volatile boolean aborted = false;

	GracefulShutdown(Tomcat tomcat) {
		this.tomcat = tomcat;
	}

	void shutDownGracefully(GracefulShutdownCallback callback) {
		logger.info("Commencing graceful shutdown. Waiting for active requests to complete");
		new Thread(() -> doShutdown(callback), "tomcat-shutdown").start();
	}

	private void doShutdown(GracefulShutdownCallback callback) {
        // Cognitive complexity starts out at 0.

		List<Connector> connectors = getConnectors();
		connectors.forEach(this::close);
		try {
            // Increments to 1 because of the `for` loop.
            // There is no indentation penalty for the `for` loop because it is
            // in a `try` block.
			for (Container host : this.tomcat.getEngine().findChildren()) {
                // Increments to 2 because of the `for` loop.
                // Increments to 3 because of the indentation level.
				for (Container context : host.findChildren()) {
                    // Increments to 4 because of the `while` loop.
                    // Increments to 6 because of the indentation level.
					while (!this.aborted && isActive(context)) {
						Thread.sleep(50);
					}
                    // Increments to 7 because of the `if` statement.
                    // Increments to 9 because of the indentation level.
					if (this.aborted) {
						logger.info("Graceful shutdown aborted with one or more requests still active");
						callback.shutdownComplete(GracefulShutdownResult.REQUESTS_ACTIVE);
                        // Increments to 10 because of early loop termination.
						return;
					}
				}
			}

		}
        // Increments to 11 because of the `catch` block.
		catch (InterruptedException ex) {
			Thread.currentThread().interrupt();
		}
		logger.info("Graceful shutdown complete");
		callback.shutdownComplete(GracefulShutdownResult.IDLE);
	}

	private List<Connector> getConnectors() {
		List<Connector> connectors = new ArrayList<>();
		for (Service service : this.tomcat.getServer().findServices()) {
			Collections.addAll(connectors, service.findConnectors());
		}
		return connectors;
	}

	private void close(Connector connector) {
		connector.pause();
		connector.getProtocolHandler().closeServerSocketGraceful();
	}

	private boolean isActive(Container context) {
		try {
			if (((StandardContext) context).getInProgressAsyncCount() > 0) {
				return true;
			}
			for (Container wrapper : context.findChildren()) {
				if (((StandardWrapper) wrapper).getCountAllocated() > 0) {
					return true;
				}
			}
			return false;
		}
		catch (Exception ex) {
			throw new RuntimeException(ex);
		}
	}

	void abort() {
		this.aborted = true;
	}

}

/*
 * Copyright 2012-2023 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
