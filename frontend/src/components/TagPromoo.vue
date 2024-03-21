<template>
    <div :class="$style.tagPromoo" :style="tagPromooStyle">
        <img :class="$style.tagPromooChild" alt="" :src="shapeDescription" />
        <div :class="$style.promoCard" />
        <h1 :class="$style.promoo">Promoção</h1>
    </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import type * as CSS from "csstype";

export default defineComponent({
    name: "TagPromoo",
    props: {
        shapeDescription: { type: String },
        propTop: { type: [Object, Array, String, Number, Boolean] },
        propLeft: { type: [Object, Array, String, Number, Boolean] },
    },
    computed: {
        tagPromooStyle(): CSS.Properties {
            return {
                top: this.propTop,
                left: this.propLeft,
            };
        },
    },
});
</script>
<style module>
.tagPromooChild {
    position: absolute;
    height: 32.33%;
    width: 16.72%;
    top: 67.67%;
    right: 83.28%;
    bottom: 0%;
    left: 0%;
    border-radius: var(--br-10xs);
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
    object-fit: contain;
}

.promoCard {
    position: absolute;
    height: 81.01%;
    width: 98.25%;
    top: 0%;
    right: 0%;
    bottom: 18.99%;
    left: 1.75%;
    border-radius: var(--br-xs);
    background-color: var(--color-gray-100);
    z-index: 1;
}

.promoo {
    margin: 0;
    position: absolute;
    height: 22.87%;
    width: 66.41%;
    top: 29.07%;
    left: 20%;
    font-size: inherit;
    font-weight: 700;
    font-family: inherit;
    display: inline-block;
    z-index: 2;
}

.tagPromoo {
    position: absolute;
    top: 93px;
    left: 0px;
    width: 515px;
    height: 258px;
    z-index: 4;
    text-align: left;
    font-size: var(--font-size-41xl);
    color: var(--color-white);
    font-family: var(--font-montserrat);
}

@media screen and (max-width: 750px) {
    .promoo {
        font-size: var(--font-size-29xl);
    }
}

@media screen and (max-width: 450px) {
    .promoo {
        font-size: var(--font-size-17xl);
    }
}
</style>