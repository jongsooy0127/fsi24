const articleFormElem = document.querySelector("#articleForm");
const articleTitleElem = document.querySelector("#articleTitle");
const articleTagElem = document.querySelector("#articleTag");
const articleAuthorElem = document.querySelector("#articleAuthor");
const articleContentElem = document.querySelector("#articleContent");

articleFormElem.addEventListener("submit", evt => {
    evt.preventDefault();

    fetch("/writearticle", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            "title": articleTitleElem.value,
            "tag": articleTagElem.value,
            "author": articleAuthorElem.value,
            "content": articleContentElem.value
        })
            .then(res => res.text())
            .then(res => {
                if (res === "OK") {
                    alert("You have submitted your article!")
                } else alert("Please try again later!")
            })
    })
})