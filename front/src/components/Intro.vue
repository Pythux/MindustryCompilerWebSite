<template>
    <pre id="presentation-typewriter">
        <span class="var-highlight">const</span> source = {
            name: <span class="string-highlight">'Master of bots'</span>,
            type: <span class="string-highlight">'Mindustry compiler'</span>,
            properties:[<span class="string-highlight">'Easy to use'</span>,
                        <span class="string-highlight">'Jump with ref'</span>,
                        <span class="string-highlight">'Open source'</span>];
        };
    </pre>
</template>

<script>

function setupTypewriter(t) {
    var HTML = t.innerHTML;

    t.innerHTML = "";

    var cursorPosition = 0,
        tag = "",
        writingTag = false,
        tagOpen = false,
        typeSpeed = 10,
        tempTypeSpeed = 0;

    var type = function () {
        if (writingTag === true) {
            tag += HTML[cursorPosition];
        }

        if (HTML[cursorPosition] === "<") {
            tempTypeSpeed = 0;
            if (tagOpen) {
                tagOpen = false;
                writingTag = true;
            } else {
                tag = "";
                tagOpen = true;
                writingTag = true;
                tag += HTML[cursorPosition];
            }
        }
        if (!writingTag && tagOpen) {
            tag.innerHTML += HTML[cursorPosition];
        }
        if (!writingTag && !tagOpen) {
            if (HTML[cursorPosition] === " ") {
                tempTypeSpeed = 0;
            } else {
                tempTypeSpeed = Math.random() * typeSpeed + 50;
            }
            t.innerHTML += HTML[cursorPosition];
        }
        if (writingTag === true && HTML[cursorPosition] === ">") {
            tempTypeSpeed = Math.random() * typeSpeed + 50;
            writingTag = false;
            if (tagOpen) {
                var newSpan = document.createElement("span");
                t.appendChild(newSpan);
                newSpan.innerHTML = tag;
                tag = newSpan.firstChild;
            }
        }

        cursorPosition += 1;
        if (cursorPosition < HTML.length - 1) {
            setTimeout(type, tempTypeSpeed);
        }
    }

    return {
        type: type,
    }
}

export default {
    mounted() {
        let typer = document.querySelector("#presentation-typewriter")
        let typewriter = setupTypewriter(typer)
        typewriter.type()
    },
}
</script>

<style lang="scss" scoped>
.var-highlight {
    color: #ff8800;
}
.string-highlight {
    color: #ffcb91;
}

#presentation-typewriter {
    font-size: 1em;
    font-family: "Courier New";
}

#presentation-typewriter:after {
    content: "|";
    animation: blink 500ms linear infinite alternate;
}

@-webkit-keyframes blink {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
}

@-moz-keyframes blink {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
}

@keyframes blink {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
}
</style>
