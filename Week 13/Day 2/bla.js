document.querySelector("#jsonForm").addEventListener("submit", evt => {
    evt.preventDefault();

    // Turn into FormData so we can get data out of the form easily.
    // You could have also put an id on each input and used
    // document.querySelector or document.getElementById to get the
    // input values. (eg. document.getElementById('colorInput').value)
    const fd = new FormData(evt.target);
    const color = fd.get("color");
    const size = fd.get("size");

    // Fetch with a POST request.
    // NOTE: JSON requests require the Content-type header to be set
    // appropriately as application/json
    const fetchOptions = {
        method: "post",
        headers: {
            "Content-type": "application/json",
        },
        // body: JSON.stringify({ color: color, size: size })
        body: JSON.stringify({ color, size })  // Same as above.
    }

    fetch("/squareJson", fetchOptions)
        .then(res => res.text())
        .then(res => {
            // The '/squareJson' endpoint returns HTML. This is not
            // typical, but to make the most of it, we're going
            // to replace a portion of the UI with the new HTML.
            document.querySelector('#stuff').innerHTML = res;
        });
})