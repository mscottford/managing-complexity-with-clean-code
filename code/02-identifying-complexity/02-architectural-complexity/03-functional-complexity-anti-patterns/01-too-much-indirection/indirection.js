// This file can be run with `node indirection.js`

function writeFormattedMessage() {
    speaker(titler(shouter(tidy(echo(messageGenerator())))))();
}
writeFormattedMessage();

var generateOutput = speaker(titler(shouter(tidy(echo(messageGenerator())))));
// Outputs "Formatted Message!!!"
generateOutput();


function speaker(target) {
    return function() {
        console.log(target());
    }
}

function echo(target) {
    return function() {
        return target();
    }
}

function messageGenerator() {
    return function() {
        return 'unformatted message';
    }
}

function tidy(target) {
    // return function that removes "un" or "Un" prefix from the result of running target
    return function() {
        return target().replace(/^un/i, '');
    }
}

function titler(target) {
    return function() {
        // return result of target formatted as Title Case
        return target().replace(/\w\S*/g, function(txt){
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
        });
    }
}

function shouter(target) {
    return function() {
        return target() + '!!!';
    }
}

