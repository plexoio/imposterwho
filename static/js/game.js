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

// enable draggables to be dropped into this
interact('.dropzone').dropzone({
    accept: '#prefix-1-drag, #suffix-1-drag',
    overlap: 0.75,

    ondropactivate: function (event) {
        event.target.classList.add('drop-active');
    },
    ondragenter: function (event) {
        const draggableElement = event.relatedTarget;
        const dropzoneElement = event.target;

        dropzoneElement.classList.add('drop-target');
        draggableElement.classList.add('can-drop');
        // draggableElement.textContent = 'Dragged in';
    },
    ondragleave: function (event) {
        event.target.classList.remove('drop-target');
        event.relatedTarget.classList.remove('can-drop');
        // event.relatedTarget.textContent = 'Dragged out';
    },
    ondrop: function (event) {
        // event.relatedTarget.textContent = 'Dropped';
    },
    ondropdeactivate: function (event) {
        event.target.classList.remove('drop-active');
        event.target.classList.remove('drop-target');
    }
});

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
        listeners: { move: dragMoveListener },
    });
