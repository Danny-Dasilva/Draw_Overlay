var canvas = document.getElementById("myCanvas");
rect = canvas.querySelector('rect')
initial_pt = canvas.querySelector('circle[fill=blue]')
current_pt = canvas.querySelector('circle[fill=red]')

function screenToSVGCoords(canvas, e) { // Read the SVG's bounding rectangle...   let canvasRect = canvas.getBoundingClientRect();    // ...and transform clientX / clientY to be relative to that rectangle   return {     x: e.clientX - canvasRect.x,     y: e.clientY - canvasRect.y   }
}
canvas.addEventListener('mousedown', e => {
    window.initial_coords = screenToSVGCoords(canvas, e);
    console.log(initial_coords) document.addEventListener('mousemove', mousemoveWithKeys);
    document.addEventListener('mouseup', mouseupWithKeys);
});

function mousemoveWithKeys(e) {
    var current_coords = screenToSVGCoords(canvas, e);
    var is_constrained = e.shiftKey;
    var is_from_center = e.altKey;
    update(initial_coords, current_coords, is_constrained, is_from_center)
}

function update(initial_coords, current_coords, is_constrained, is_from_center) { // let description = describe(`updates the rectangle \`rect\``);     let current_x = current_coords.x;     let current_y = current_coords.y;          if (is_constrained) {                  // compute the distance on the X and Y coordiantes...             let deltaX = current_coords.x - initial_coords.x;             let deltaY = current_coords.y - initial_coords.y;                  // ...then find whichever is largest...             let delta = Math.max(Math.abs(deltaX), Math.abs(deltaY));                      // ...which we then apply to both the X and Y coordinates         current_x = initial_coords.x + (Math.sign(deltaX) || 1) * delta;             current_y = initial_coords.y + (Math.sign(deltaY) || 1) * delta;                  }          let x, y;          let width = Math.abs(current_x - initial_coords.x);     let height = Math.abs(current_y - initial_coords.y);          if (is_from_center) {                  let reflected_x = 2 * initial_coords.x - current_x;         let reflected_y = 2 * initial_coords.y - current_y;                  x = Math.min(reflected_x, current_x);         y = Math.min(reflected_y, current_y);                  width = 2 * width;         height = 2 * height;          } else {                  x = Math.min(initial_coords.x, current_x);         y = Math.min(initial_coords.y, current_y);          }          rect.setAttribute('x', x);     rect.setAttribute('y', y);     rect.setAttribute('width', width);     rect.setAttribute('height', height);     initial_pt.setAttribute('cx', initial_coords.x);     initial_pt.setAttribute('cy', initial_coords.y);     current_pt.setAttribute('cx', current_coords.x);     current_pt.setAttribute('cy', current_coords.y);          // return description;
}

function mousedownWithKeys(e) {
    var initial_coords = screenToSVGCoords(canvas, e);
    document.addEventListener('mousemove', mousemoveWithKeys);
    document.addEventListener('mouseup', mouseupWithKeys);
}

function mouseupWithKeys(e) {
    document.removeEventListener('mousemove', mousemoveWithKeys);
    document.removeEventListener('mouseup', mouseupWithKeys);
}

function updateDropdown() {
    console.log("uopdate") $.getJSON('/static/data.json', function(data) {
        var select = document.getElementById("select");
        const objData = Object.entries(data) select.options.length = 0;
        for (const [key, value] of objData) {
            var option = document.createElement("option");
            option.text = key;
            select.add(option);
        }
    });
};
updateDropdown()

function loadCoords() {
    var select = document.getElementById("select").value $.getJSON('static/data.json', function(data) {
        const objData = Object.entries(data) for (const [key, value] of objData) {
            if (key === select) {
                console.log(value) rect.setAttribute('x', value.x);
                rect.setAttribute('y', value.y);
                rect.setAttribute('width', value.width);
                rect.setAttribute('height', value.height);
                initial_pt.setAttribute('cx', value.x);
                initial_pt.setAttribute('cy', value.y);
                current_pt.setAttribute('cx', parseInt(value.x) + parseInt(value.width));
                current_pt.setAttribute('cy', parseInt(value.y) + parseInt(value.height));
            }
        }
    })
}

function addProfile() {
    t = document.getElementById("name").value x = rect.getAttribute('x');
    y = rect.getAttribute('y');
    rx = rect.getAttribute('rx');
    ry = rect.getAttribute('ry');
    width = rect.getAttribute('width');
    height = rect.getAttribute('height');
    console.log(t, x, y, width, height);
    $.ajax({
        type: 'POST',
        beforeSend: function(request) {
            request.setRequestHeader("Authority", JSON.stringify({
                [t]: {
                    'x': x,
                    'y': y,
                    'width': width,
                    'height': height
                }
            }));
        },
        url: "/add_profile",
        contentType: 'application/json;charset=UTF-8',
        data: "json: " + JSON.stringify({
            [t]: {
                'x': x,
                'y': y,
                'width': width,
                'height': height
            }
        }),
    });
    updateDropdown()
}

function deleteProfile() {
    var select = document.getElementById("select");
    console.log(select.value) $.ajax({
        type: 'POST',
        beforeSend: function(request) {
            request.setRequestHeader("Authority", JSON.stringify(select.value));
        },
        url: "/delete_profile",
        contentType: 'application/json;charset=UTF-8',
        data: "json: " + JSON.stringify(select.value),
    });
    updateDropdown()
}