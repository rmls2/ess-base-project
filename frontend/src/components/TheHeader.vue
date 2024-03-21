<template>
    <div :class="$style.header2">
      <footer :class="$style.header2Child" />
      <img :class="$style.header2Item" alt="" src="../assets/rectangle-1116.svg" />
      <img
        :class="$style.undrawMaleAvatarG98d3Icon"
        alt=""
        src="../assets/rooms/undraw-male-avatar-g98d-3.svg"
      />
      <div :class="$style.quartosBoxParent">
        <div :class="$style.quartosBox">
          <img
            :class="$style.quartosBoxChild"
            loading="lazy"
            alt=""
            src="../assets/rooms/rectangle-450.svg"
          />
          <b :class="$style.hotelaria">HOTELARIA</b>
        </div>
        <div :class="$style.homeFrameset">
          <div :class="$style.homeSections">
            <div :class="$style.home">Home</div>
            <RouterLink to="/rooms-page" :class="$style.quartos">Quartos</RouterLink>
            <div :class="$style.atraes" @click="onAtraesTextClick">
              <p :class="$style.atraes1">Atrações</p>
            </div>
          </div>
        </div>
      </div>
      <div :class="$style.avatarInstance">
        <img :class="$style.avatarIcon" loading="lazy" alt="" src="../assets/avatar.svg" />
      </div>
    </div>
  </template>
  <script lang="ts">
    import { defineComponent } from "vue";
    import { RouterLink } from 'vue-router'

    export default defineComponent({
      name: "The-Header",
      methods: {
        onAtraesTextClick() {
          // Please sync "Atração Desktop" to the project
        },
      },
    });
  </script>
  <style module>
    .header2Child {
      height: 100%;
      width: 100%;
      position: absolute;
      margin: 0 !important;
      top: 0px;
      right: 0px;
      bottom: 0px;
      left: 0px;
      background-color: rgba(255, 255, 255, 0);
    }
    .header2Item {
      height: 118px;
      width: 100%;
      position: absolute;
      margin: 0 !important;
      top: 0px;
      right: 0px;
      left: 0px;
      max-width: 100%;
      overflow: hidden;
      z-index: 1;
    }
    .undrawMaleAvatarG98d3Icon {
      height: 97px;
      width: 97px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      display: none;
      z-index: 2;
    }
    .quartosBoxChild {
      position: absolute;
      top: 0px;
      left: 0px;
      width: 256px;
      height: 149px;
      z-index: 2;
    }
    .hotelaria {
      position: absolute;
      top: 59px;
      left: 40px;
      letter-spacing: 0.15em;
      z-index: 3;
    }
    .quartosBox {
      height: 149px;
      width: 256px;
      position: relative;
    }
    .home {
      height: 36px;
      width: 90px;
      position: relative;
      font-weight: 500;
      display: inline-block;
      flex-shrink: 0;
      z-index: 2;
    }
    .quartos {
      height: 36px;
      width: 114px;
      position: relative;
      font-weight: 500;
      display: inline-block;
      flex-shrink: 0;
      z-index: 2;
    }
    .atraes1 {
      margin: 0;
    }
    .atraes {
      height: 40px;
      flex: 1;
      position: relative;
      font-weight: 500;
      display: inline-block;
      cursor: pointer;
      z-index: 2;
    }
    .homeSections {
      align-self: stretch;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: 0px 32.5px;
    }
    .homeFrameset {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: 47px 0px 0px;
      box-sizing: border-box;
      max-width: 100%;
      font-size: var(--font-size-6xl);
      color: var(--color-white);
    }
    .quartosBoxParent {
      width: 727px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: 0px 76px;
      max-width: 100%;
    }
    .avatarIcon {
      width: 97px;
      height: 97px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      z-index: 2;
    }
    .avatarInstance {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: 11px 0px 0px;
    }
    .header2 {
      width: 100%;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: space-between;
      padding: 0px 23px 7px 75px;
      box-sizing: border-box;
      position: sticky;
      top: 0;
      z-index: 99;
      letter-spacing: normal;
      gap: 20px;
      text-align: left;
      font-size: 24px;
      color: #8b4513;
      font-family: var(--font-montserrat);
    }
  
    @media screen and (max-width: 825px) {
      .homeSections {
        display: none;
      }
  
      .quartosBoxParent {
        gap: 0px 38px;
      }
  
      .header2 {
        padding-left: 37px;
        box-sizing: border-box;
      }
    }
    @media screen and (max-width: 450px) {
      .hotelaria {
        font-size: 19px;
      }
  
      .homeSections {
        gap: 0px 16px;
      }
  
      .quartosBoxParent {
        gap: 0px 19px;
      }
    }
  </style>
  