// AI generated
function dragMoveListener(event) {
    const target = event.target;
    const x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx;
    const y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

    // Translate the element
    target.style.transform = `translate(${x}px, ${y}px)`;

    // Update the position attributes
    target.setAttribute('data-x', x);
    target.setAttribute('data-y', y);
}

// Get the position of the dropzone and update dynamically
let prefixRect;
let suffixRect;
let prefixCenter;
let suffixCenter;

// Gets the positions of the dropzones
function updateDropzoneRect() {
    const prefixDropzone = document.getElementById("prefix-dropzone");
    prefixRect = prefixDropzone.getBoundingClientRect();

    const suffixDropzone = document.getElementById("suffix-dropzone");
    suffixRect = suffixDropzone.getBoundingClientRect();

    // Update the center positions of the dropzones
    updateDropzoneCenter();
}

// Calculates the center of the dropzones for snapping position
function updateDropzoneCenter() {
    prefixCenter = {
        x: prefixRect.left + prefixRect.width / 2,
        y: prefixRect.top + prefixRect.height / 2,
    };

    suffixCenter = {
        x: suffixRect.left + suffixRect.width / 2,
        y: suffixRect.top + suffixRect.height / 2,
    };
}

// initial calculation of the dropzone position
updateDropzoneRect();

// event listener for screen resize/rotate
window.addEventListener('resize', updateDropzoneRect);
window.addEventListener('orientationchange', updateDropzoneRect);

// Audio placeholders
// const dragStartAudio = new Audio('drag-start.mp3'); // Replace with actual file
// const dragSnapAudio = new Audio('drag-snap.mp3'); // Replace with actual file
// const dropAudio = new Audio('drop.mp3'); // Replace with actual file

// Track the current draggable pair in the dropzones
let currentPrefix = null;
let currentSuffix = null;

// Enable/disable the submit button
function updateSubmitButtonState() {
    const button = document.getElementById('submit-button');
    if (currentPrefix && currentSuffix) {
        button.disabled = false;
        button.classList.remove('btn-secondary');
        button.classList.add('btn-primary');
    } else {
        button.disabled = true;
        button.classList.remove('btn-primary');
        button.classList.add('btn-secondary');
    }
}

// Handle the submit button click
document.getElementById('submit-button').addEventListener('click', () => {
    if (!currentPrefix || !currentSuffix) return;

    // Transition the suffix text
    transitionSuffix(currentSuffix, true);

    // Simultaneously start the background color transition for prefix
    currentPrefix.style.transition = 'background-color 2s';
    currentPrefix.style.backgroundColor = '#4e4'; // Green
});

// Get the positive replacement for a suffix
function getPositiveReplacement(negativeText) {
    const replacements = {
        'not enough.': 'enough.',
        "can't do this.": 'can do this.',
        "won't make it.": 'will make it.',
    };
    return replacements[negativeText] || negativeText;
}

// Helper function to get the negative replacement for a suffix
function getNegativeReplacement(positiveText) {
    const replacements = {
        'enough.': 'not enough.',
        'can do this.': "can't do this.",
        'will make it.': "won't make it.",
    };
    return replacements[positiveText] || positiveText;
}

// Function to transition suffix text and background color
function transitionSuffix(suffixElement, isPositive) {
    const suffixTextElement = suffixElement.querySelector('.drag-text');
    const suffixText = suffixTextElement.textContent.trim();

    // Determine the new text and background color
    const newText = isPositive ? getPositiveReplacement(suffixText) : getNegativeReplacement(suffixText);
    const newBackgroundColor = isPositive ? '#4e4' : '#29e'; // Green for positive, blue for negative

    // Start fade-out for the current suffix text
    suffixTextElement.style.transition = 'opacity 1s';
    suffixTextElement.style.opacity = '0';

    // After 1 second, replace the text and start fade-in
    setTimeout(() => {
        suffixTextElement.textContent = newText;
        suffixTextElement.style.opacity = '0'; // Ensure it remains invisible before fade-in
        suffixTextElement.style.transition = 'opacity 1s';
        suffixTextElement.style.opacity = '1'; // Start fade-in

        // Simultaneously start the background color transition
        suffixElement.style.transition = 'background-color 2s';
        suffixElement.style.backgroundColor = newBackgroundColor;
    }, 1000);
}

// Function to reset a draggable element (prefix or suffix) when dragged out of the dropzone
function resetDraggable(draggableElement, isPrefix) {
    const textElement = draggableElement.querySelector('.drag-text');
    const currentText = textElement.textContent.trim();

    // Skip reset if the suffix already has the negative text
    if (!isPrefix && currentText === getNegativeReplacement(currentText)) {
        console.log('Suffix already has negative text, skipping reset.');
        return;
    }

    // Clear the text instantly for suffix and fade in the negative text
    if (!isPrefix) {
        const negativeText = getNegativeReplacement(currentText);
        textElement.textContent = negativeText;
        textElement.style.transition = 'opacity 1s';
        textElement.style.opacity = '0';

        setTimeout(() => {
            textElement.style.opacity = '1'; // Fade in the negative text
        }, 0); // No delay for clearing the text
    }

    // Reset the background color to blue
    draggableElement.style.transition = 'background-color 2s';
    draggableElement.style.backgroundColor = '#29e'; // Blue

    // Ensure the draggable can re-trigger dropzone events
    draggableElement.classList.remove('can-drop'); // Remove any lingering state
}

// Updated dropzone logic to handle drag-away reset
function setupDropzone(dropzoneId, draggableClass) {
    interact(`#${dropzoneId}`).dropzone({
        accept: `.${draggableClass}`,
        overlap: 0.75,

        ondropactivate: function (event) {
            event.target.classList.add('drop-active');
        },
        ondragenter: function (event) {
            const draggableElement = event.relatedTarget;
            const dropzoneElement = event.target;

            // Transition the draggable's background color to green
            draggableElement.style.transition = 'background-color 2s';
            draggableElement.style.backgroundColor = '#4e4'; // Green

            dropzoneElement.classList.add('drop-target');
            draggableElement.classList.add('can-drop');

            if (dropzoneId === 'prefix-dropzone') {
                currentPrefix = draggableElement;
            } else if (dropzoneId === 'suffix-dropzone') {
                currentSuffix = draggableElement;
            }

            updateSubmitButtonState();
        },
        ondragleave: function (event) {
            const draggableElement = event.relatedTarget;
            const dropzoneElement = event.target;

            // Transition the draggable's background color back to blue
            draggableElement.style.transition = 'background-color 2s';
            draggableElement.style.backgroundColor = '#29e'; // Blue

            dropzoneElement.classList.remove('drop-target');
            draggableElement.classList.remove('can-drop');

            if (dropzoneId === 'prefix-dropzone') {
                resetDraggable(draggableElement, true); // Reset prefix
                currentPrefix = null;
            } else if (dropzoneId === 'suffix-dropzone') {
                resetDraggable(draggableElement, false); // Reset suffix
                currentSuffix = null;
            }

            updateSubmitButtonState();
        },
        ondrop: function (event) {
            // dropAudio.play();
        },
        ondropdeactivate: function (event) {
            event.target.classList.remove('drop-active');
            event.target.classList.remove('drop-target');
        },
    });
}

// Only allow prefixes to be dropped in prefix dropzone, and suffixes in suffix dropzone
setupDropzone('prefix-dropzone', 'prefix');
setupDropzone('suffix-dropzone', 'suffix');

// interact.js drag and drop example code
// https://interactjs.io/  Drag and Drop
interact('.drag-drop')
    .draggable({
        inertia: true,
        modifiers: [
            // interact.js targets snap function
            // https://interactjs.io/docs/snapping/#targets-option
            interact.modifiers.snap({
                targets: [
                    // prefix snapping to dropzone center
                    function (x, y, interaction) {
                        // Dynamically return the updated dropzone position
                        return {
                            x: prefixCenter.x,
                            y: prefixCenter.y,
                            range: 50,
                        };
                    },
                    // suffix snapping to dropzone center
                    function (x, y, interaction) {
                        return {
                            x: suffixCenter.x,
                            y: suffixCenter.y,
                            range: 50,
                        };
                    },
                ],
            }),
        ],
        autoScroll: true,
        listeners: {
            start(event) {
                // dragStartAudio.play();
            },
            move: dragMoveListener,
            end(event) {
                // dragSnapAudio.play();
            },
        },
    });
