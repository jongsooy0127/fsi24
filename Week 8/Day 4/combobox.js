function activateInput(primaryObj, objectElem, matchFunction) {
    // Get the variables to the stuff in the DOM tree.
    /*          const inputElem = document.querySelector(inputDOM);
        const matchesElem = document.querySelector(matchDOM);
        const buttonElem = document.querySelector(btnDOM);
        const infoElem = document.querySelector(infoPanelDOM); */
    const { inputElem, matchesElem, buttonElem, infoElem } = objectElem

    function setInputValue(focusedName) {
        inputElem.value = focusedName;  // Make input match what we clicked on.
        inputElem.focus();

        // Blank out the matches, once we've clicked on an item in the list.
        // matchesElem.innerHTML = "";
        matchesElem.replaceChildren();//⚠️quick way to remove child.
        matchesElem.style.display = "none";
    }

    function submitChoice() {
        // Find the school that matches what we typed into the input.
        const matchingItem =
            primaryObj //first item that matches will be shown
                .filter(search => search !== null)
                .find(search => search.strDrink.toLowerCase() === inputElem.value.toLowerCase())

        // Since Array.prototype.find returns an undefined if it doesn't find a match, we test for it.
        if (matchingItem !== undefined) {  // If we found a match...
            // console.log("DETAILS:", matchingItem);

            matchesElem.replaceChildren();
            matchesElem.style.display = "none";
            matchFunction(matchingItem, infoElem);
            // Fill in the matchingItem inside the info area.
            /*             let newHtml = `<div>Name: ${matchingItem.name}</div>`;
            
                        // for (let i = 0; i < matchingItem.web_pages.length; i++) {
                        //     const link = matchingItem.web_pages[i];
                        for (const link of matchingItem.web_pages) {  // for of loop
                            newHtml += `<div>Pages: <a href="${link}" target="_blank">${link}</a></div>`
                        }
                        newHtml += `<div>Country: ${matchingItem.country}</div>`;
            
                        infoElem.innerHTML = newHtml; */
        }
    }

    inputElem.addEventListener("input", () => {
        if (inputElem.value.length > 1) {
            // let matchingSchoolNames =
            // primaryObj
            //     .filter(school => school.name.toLowerCase().includes(inputElem.value.toLowerCase()))
            //     .map(school => school.name);
            // primaryObj
            //     .map(school => school.name)
            //     .filter(school => school.toLowerCase().includes(inputElem.value.toLowerCase()))

            // matchesElem.innerHTML = "";  // 1st step: Clear out old matches/refresh
            matchesElem.replaceChildren(); // 1st step: Clear out old matches/refresh

            // Add new matches.
            matchesElem.style.display = "block";
            console.log(primaryObj)
            primaryObj
                .filter(search => search !== null)
                .filter(search => {
                    return search.strDrink.toLowerCase().includes(inputElem.value.toLowerCase());
                })//filter according to input
                .forEach((search, i) => {//for each filtered element:
                    // Create new item to add to matches list.
                    const newItem = document.createElement("a");
                    // newItem.href="#";
                    newItem.tabIndex = i;  // For the focus through "tab" key to work properly.
                    newItem.innerHTML = search.strDrink;
                    matchesElem.appendChild(newItem);

                    newItem.addEventListener("click", () => {
                        setInputValue(search.strDrink);  // Make input match what we clicked on.
                    });

                    newItem.addEventListener("keydown", (evt) => {
                        if (i > 0 && evt.key === "ArrowUp") {
                            matchesElem.children[i - 1].focus();
                            inputElem.value = matchesElem.children[i - 1].innerHTML;
                        }
                        else if (i < matchesElem.children.length - 1 && evt.key === "ArrowDown") {
                            matchesElem.children[i + 1].focus();
                            inputElem.value = matchesElem.children[i + 1].innerHTML;
                        }
                        else if (evt.key === "Enter") {
                            setInputValue(search.strDrink);
                        }
                    });

                    // newItem.addEventListener("keyup", (evt) => {
                    //     if (evt.key === "Enter") {
                    //         setInputValue(school.name);
                    //     }
                    // });
                })
        }
    });

    inputElem.addEventListener("keyup", (evt) => {
        // console.log("INPUT EVENT:", evt);
        if (matchesElem.style.display !== "none" && evt.key === "ArrowDown") {
            // console.log("MATCH:", matchesElem.children[0]);
            matchesElem.children[0].focus();
        }
        else if (evt.key === "Enter") {
            matchesElem.replaceChildren();
            submitChoice();
        }
    });

    buttonElem.addEventListener("click", submitChoice)
}