document.addEventListener("click", function (e) {
    if (e.target.classList.contains("like-btn")) {
        const button = e.target;
        const postId = button.dataset.postId;

        if (!postId) return;

        fetch(`/posts/${postId}/like/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
        })
        .then(response => {
             if (!response.ok) {
                 throw new Error("Network response was not ok");
             }
             return response.json();
        })
        .then(data => {
            // Update the like count span next to the button
            const likeCount = document.getElementById(`like-count-${postId}`);
            if (likeCount) {
                likeCount.textContent = data.like_count;
            }

            // Update button text
            button.textContent = data.liked ? "Unlike" : "Like";
            
            // Optional: Update style based on state (e.g. text color)
            if (data.liked) {
                button.classList.add('text-blue-500', 'font-bold');
            } else {
                button.classList.remove('text-blue-500', 'font-bold');
            }
        })
        .catch(error => console.error("Error liking post:", error));
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

// Infinite Scroll
let page = 2;
let loading = false;

window.addEventListener("scroll", function () {
    if (loading) return;

    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
        const loadingElement = document.getElementById("loading");
        if (!loadingElement) return;

        loading = true;
        loadingElement.style.display = "block";

        fetch(`?page=${page}`, {
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("post-container");
            
            if (data.html && container) {
                container.insertAdjacentHTML("beforeend", data.html);
            }

            if (data.has_next) {
                page += 1;
                loading = false;
            } else {
                loadingElement.innerText = "No more posts";
            }
        })
        .catch(err => {
            console.error("Infinite scroll error:", err);
            loading = false;
        });
    }
});
