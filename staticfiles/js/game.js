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
const dragStartAudio = new Audio('drag-start.mp3'); // Replace with actual file
const dragSnapAudio = new Audio('drag-snap.mp3'); // Replace with actual file
const dropAudio = new Audio('drop.mp3'); // Replace with actual file

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

    console.log('Submit button clicked');

    // Transition the suffix text
    const suffixTextElement = currentSuffix.querySelector('.drag-text');
    const suffixText = suffixTextElement.textContent.trim();
    const positiveText = getPositiveReplacement(suffixText);

    // Start fade-out for the negative suffix text
    suffixTextElement.style.transition = 'opacity 1s';
    suffixTextElement.style.opacity = '0';
    console.log('Starting fade-out for suffix text');

    // After 1 second, replace the text and start fade-in
    setTimeout(() => {
        suffixTextElement.textContent = positiveText;
        suffixTextElement.style.opacity = '0'; // Ensure it remains invisible before fade-in
        suffixTextElement.style.transition = 'opacity 1s';
        suffixTextElement.style.opacity = '1'; // Start fade-in
        console.log('Replaced suffix text with positive version and started fade-in');

        // Simultaneously start the background color transition
        currentPrefix.style.transition = 'background-color 2s';
        currentSuffix.style.transition = 'background-color 2s';
        currentPrefix.style.backgroundColor = '#4e4'; // Green
        currentSuffix.style.backgroundColor = '#4e4'; // Green
        console.log('Started background color transition');
    }, 1000);

    // After 2 seconds, reveal the hidden pair
    setTimeout(() => {
        const hiddenPair = document.querySelector('.hidden');
        if (hiddenPair) {
            hiddenPair.classList.remove('hidden');
            console.log('Revealed hidden pair');
        }
    }, 2000);

    // After 4 seconds, hide the current pair and reset their positions
    setTimeout(() => {
        currentPrefix.classList.add('hidden');
        currentSuffix.classList.add('hidden');
        console.log('Hid current pair and reset state');

        // Reset the current pair variables
        currentPrefix = null;
        currentSuffix = null;

        // Update the submit button state
        updateSubmitButtonState();
    }, 4000);
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

// Function to setup dropzones
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

            dropzoneElement.classList.remove('drop-target');
            draggableElement.classList.remove('can-drop');

            if (dropzoneId === 'prefix-dropzone') {
                currentPrefix = null;
            } else if (dropzoneId === 'suffix-dropzone') {
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
                // Dynamically calculate the offset to align the draggable's top-left corner
                // offset: { x: 20, y: 20 },
            }),
            // interact.modifiers.restrictRect({
            //     restriction: 'parent',
            //     endOnly: true,
            // }),
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
