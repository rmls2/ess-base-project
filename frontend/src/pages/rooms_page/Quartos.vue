<template>
  <div :class="$style.quartos">
    <img :class="$style.union3Icon" alt="" src="../../assets/promotions/union-3.svg" />
    <div :class="$style.bemVindo">
      <img :class="$style.maskGroupIcon" alt="" src="../../assets/promotions/mask-group@2x.png" />
      <div :class="$style.header">
        <div :class="$style.headerChild" />
        <img :class="$style.headerItem" alt="" src="../../assets/promotions/rectangle-1116.svg" />
        <div :class="$style.hotelBrandSymbol">
          <div :class="$style.simboloHotelaria">
            <img :class="$style.simboloHotelariaChild" loading="lazy" alt=""
              src="../../assets/promotions/rectangle-450.svg" />
            <b :class="$style.hotelaria">HOTELARIA</b>
          </div>
          <div :class="$style.promotionTags">
            <div :class="$style.pginas">
              <div :class="$style.home">Home</div>
              <div :class="$style.promotionTags1">
                <div :class="$style.quartos1">Quartos</div>
              </div>
              <div :class="$style.atraes" @click="onAtraesTextClick">
                <p :class="$style.atraes1">Atrações</p>
              </div>
            </div>
          </div>
        </div>
        <div :class="$style.rectangleShapes">
          <img :class="$style.undrawMaleAvatarG98d3Icon" loading="lazy" alt=""
            src="../../assets/promotions/undraw-male-avatar-g98d-3.svg" />
        </div>
      </div>
      <div :class="$style.rectangleShapes1">
        <div :class="$style.rectangleShapes2">
          <h1 :class="$style.bemVindoA">Bem vindo a</h1>
          <h1 :class="$style.hotelaria1">HOTELARIA</h1>
        </div>
      </div>
      <div :class="$style.headerInstance">
        <div :class="$style.scrollParent">
          <b :class="$style.scroll">Scroll</b>
          <div :class="$style.subtractionVector">
            <img :class="$style.subtraction2Icon" loading="lazy" alt=""
              src="../../assets/promotions/subtraction-2.svg" />
          </div>
        </div>
      </div>
    </div>
    <main :class="$style.noiteEstreladaGroup">
      <section :class="$style.atualizarPromocaoInstanceParent">
        <div :class="$style.atualizarPromocaoInstance">
          <h1 :class="$style.quartos2">QUARTOS</h1>
        </div>
        <div :class="$style.rRDiaLine">
          <div :class="$style.rectangleParent">
            <div :class="$style.frameChild" />
            <div :class="$style.devonJanseVanRensburgWedfParent">
              <img :class="$style.devonJanseVanRensburgWedfIcon" alt=""
                src="../../assets/promotions/devonjansevanrensburg-wedftzv0quunsplash-1@2x.png" />
              <div :class="$style.frameTriplet" />
              <div :class="$style.rectangleGroup">
                <div :class="$style.frameItem" />
                <h1 :class="$style.noiteEstrelada" ref="quartoCometaRef">QUARTO COMETA</h1>
              </div>
              <img :class="$style.frameInner" loading="lazy" alt="" src="../../assets/promotions/group-65.svg" />
            </div>
            <div :class="$style.rRDiaTextWrapper">
              <div :class="$style.rRDiaText">
                <div :class="$style.informaesWrapper">
                  <div :class="$style.informaes">
                    <img :class="$style.informaesChild" loading="lazy" alt=""
                      src="../../assets/promotions/group-58.svg" />
                    <div :class="$style.header1">
                      <b :class="$style.informaes1">INFORMAÇÕES</b>
                    </div>
                  </div>
                </div>
                <button v-if="mostrarBotaoCadastro" :class="$style.cadastrarPromooWrapper" @click="onGroupButtonClick">
                  <div :class="$style.cadastrarPromoo">
                    <img :class="$style.cadastrarPromooChild" alt="" src="../../assets/promotions/rectangle-1091.svg" />
                    <b :class="$style.cadastrarPromoo1">Cadastrar promoção</b>
                  </div>
                </button>
                <button :class="$style.rADailyRate">
                  <img :class="$style.rADailyRateChild" alt="" src="../../assets/promotions/rectangle-1090.svg" />
                  <b :class="$style.r147Diria">R$ 147 Diária</b>
                </button>
              </div>
            </div>
          </div>
          <!-- <div :class="$style.frameParent">
            <div :class="$style.rectangleContainer">
              <div :class="$style.rectangleDiv" />
              <div :class="$style.atualizarPromocao">
                <div :class="$style.excluirPromocao">
                  <img :class="$style.maskGroupIcon1" alt="" src="../../assets/promotions/mask-group-1@2x.png" />
                  <div :class="$style.subRoomFrame" />
                  <img :class="$style.excluirPromocaoChild" loading="lazy" alt=""
                    src="../../assets/promotions/group-65.svg" />
                </div>
              </div>
              <div :class="$style.frameWrapper">
                <div :class="$style.groupDiv">
                  <div :class="$style.frameChild1" />
                  <h1 :class="$style.noiteEstrelada1">NOITE ESTRELADA</h1>
                </div>
              </div>
              <div :class="$style.starBackground">
                <div :class="$style.infoFrame">
                  <div :class="$style.promoText">
                    <div :class="$style.informaes2">
                      <img :class="$style.informaesItem" alt="" src="../../assets/promotions/group-58.svg" />
                      <div :class="$style.roomLabel">
                        <b :class="$style.informaes3">INFORMAÇÕES</b>
                      </div>
                    </div>
                  </div>
                  <div :class="$style.updatePromo">
                    <button :class="$style.atualizarpromoo">
                      <img :class="$style.atualizarpromooChild" alt=""
                        src="../../assets/promotions/rectangle-1091-1.svg" />
                      <b :class="$style.atualizarPromoo">Atualizar promoção</b>
                    </button>
                    <div :class="$style.excluir">
                      <img :class="$style.excluirChild" alt="" src="../../assets/promotions/ellipse-5.svg" />
                      <img :class="$style.lixeiraDeReciclagem1Icon" loading="lazy" alt=""
                        src="../../assets/promotions/lixeiradereciclagem-1@2x.png" />
                    </div>
                  </div>
                  <div :class="$style.infoTag">
                    <img :class="$style.infoTagChild" alt="" src="../../assets/promotions/rectangle-1090.svg" />
                    <div :class="$style.deleteTag">
                      <b :class="$style.r155R150DiriaContainer">
                        <span>R$155</span>
                        <span :class="$style.r150Diria"> R$150 Diária</span>
                      </b>
                      <img :class="$style.deleteTagChild" loading="lazy" alt=""
                        src="../../assets/promotions/line-8.svg" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div :class="$style.tagPromoo">
              <img :class="$style.tagPromooChild" alt="" src="../../assets/promotions/polygon-1.svg" />
              <div :class="$style.promoCard" />
              <h1 :class="$style.promoo">Promoção</h1>
            </div>
          </div> -->
          <!-- <div :class="$style.tag">
            <div :class="$style.rectangleParent1">
              <div :class="$style.frameChild2" />
              <div :class="$style.image">
                <img :class="$style.fredKleberGtbaxavlvsgUnsplaIcon" alt=""
                  src="../../assets/promotions/fredklebergtbaxavlvsgunsplash-1@2x.png" />
                <div :class="$style.imageChild" />
                <img :class="$style.imageItem" alt="" src="../../assets/promotions/group-65.svg" />
              </div>
              <div :class="$style.group">
                <div :class="$style.rectangleParent2">
                  <div :class="$style.frameChild3" />
                  <h1 :class="$style.noiteEstrelada2">NOITE ESTRELADA</h1>
                </div>
              </div>
              <img :class="$style.groupIcon" alt="" src="../../assets/promotions/group-87@2x.png" />
              <div :class="$style.atualizarPromoo1">
                <div :class="$style.rectangle">
                  <div :class="$style.rRDiria">
                    <div :class="$style.informaes4">
                      <img :class="$style.informaesInner" alt="" src="../../assets/promotions/group-58.svg" />
                      <div :class="$style.iNFORMAES">
                        <b :class="$style.informaes5">INFORMAÇÕES</b>
                      </div>
                    </div>
                  </div>
                  <div :class="$style.atualizarPromoo2">
                    <button :class="$style.atualizarpromoo1">
                      <img :class="$style.atualizarpromooItem" alt=""
                        src="../../assets/promotions/rectangle-1091-1.svg" />
                      <b :class="$style.atualizarPromoo3">Atualizar promoção</b>
                    </button>
                    <div :class="$style.excluir1">
                      <img :class="$style.excluirItem" alt="" src="../../assets/promotions/ellipse-5.svg" />
                      <img :class="$style.lixeiraDeReciclagem1Icon1" alt=""
                        src="../../assets/promotions/lixeiradereciclagem-1@2x.png" />
                    </div>
                  </div>
                  <div :class="$style.ratesBox">
                    <img :class="$style.ratesBoxChild" alt="" src="../../assets/promotions/rectangle-1090.svg" />
                    <div :class="$style.lineSeparator">
                      <b :class="$style.r155R150DiriaContainer1">
                        <span>R$155</span>
                        <span :class="$style.r150Diria1"> R$150 Diária</span>
                      </b>
                      <img :class="$style.lineSeparatorChild" alt="" src="../../assets/promotions/line-8.svg" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div :class="$style.tagPromoo1">
              <img :class="$style.tagPromooItem" alt="" src="../../assets/promotions/polygon-1.svg" />
              <div :class="$style.rectangleShape" />
              <h1 :class="$style.promoo1">Promoção</h1>
            </div>
          </div> -->
        </div>
        <!-- <div :class="$style.groupedFrames">
          <div :class="$style.pathNavigation">
            <img :class="$style.pathNavigationChild" loading="lazy" alt="" src="../../assets/promotions/group-40.svg" />
            <img :class="$style.pathNavigationItem" loading="lazy" alt="" src="../../assets/promotions/group-39.svg" />
          </div>
        </div> -->
      </section>
    </main>
    <div :class="$style.textAtFooter">
      <b :class="$style.footer">FOOTER</b>
    </div>
  </div>
</template>
<script lang="ts">
import { useApiService, PromotionModel, PromotionUpdateModel } from '../../services/apiService';
import { defineComponent } from "vue";

const { getPromotion, getCurrentPromotion, getRoomId, createPromotion, updatePromotion, deletePromotion } = useApiService();

export default defineComponent({
  name: "Quartos",
  data() {
    return {
      mostrarBotaoCadastro: false,
    };
  },
  async mounted() {
    try {
      // Implemente a lógica de verificação na API durante o mounted
      const quartoCometaElement = this.$refs.quartoCometaRef.innerText.toLowerCase();
      const roomId = (await getRoomId(quartoCometaElement)).data.room_id
      const resultadoVerificacao = await getPromotion(roomId);
      var ver = false
      if (resultadoVerificacao.data){
        ver = true
      }
      // Defina mostrarBotaoCadastro com base no resultado da verificação
      this.mostrarBotaoCadastro = ver;
    } catch (error) {
      console.error("Erro ao verificar promoção durante o mounted:", error);
    }
  },
  methods: {
    onAtraesTextClick() {
      // Please sync "Atração Desktop" to the project
    },
    onGroupButtonClick() {
      // Please sync "Promoção" to the project
    },
    putRoomValue(){
      
    }
  },
});
</script>
<style module>
.union3Icon {
  width: 1920px;
  height: 321px;
  position: absolute;
  margin: 0 !important;
  bottom: 0px;
  left: -1px;
  flex-shrink: 0;
}

.maskGroupIcon {
  width: 100%;
  height: 100%;
  position: absolute;
  margin: 0 !important;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
  object-fit: cover;
}

.headerChild {
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

.headerItem {
  height: 150.5px;
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

.simboloHotelariaChild {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
}

.hotelaria {
  position: absolute;
  top: 39.61%;
  left: 15.62%;
  letter-spacing: 0.15em;
  z-index: 1;
}

.simboloHotelaria {
  height: 190.1px;
  width: 341.3px;
  position: relative;
  min-width: 341.3px;
  max-width: 100%;
  z-index: 2;
}

.home {
  height: 45.9px;
  width: 120px;
  position: relative;
  font-weight: 500;
  display: inline-block;
  flex-shrink: 0;
}

.quartos1 {
  align-self: stretch;
  height: 45.9px;
  position: relative;
  font-weight: 500;
  display: inline-block;
  flex-shrink: 0;
}

.promotionTags1 {
  width: 156.1px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 4px 0px 0px;
  box-sizing: border-box;
}

.atraes1 {
  margin: 0;
}

.atraes {
  height: 51px;
  width: 168px;
  position: relative;
  font-weight: 500;
  display: inline-block;
  flex-shrink: 0;
  cursor: pointer;
}

.pginas {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 41.3px;
  z-index: 2;
}

.promotionTags {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 68.89999999999998px 0px 0px;
  box-sizing: border-box;
  min-width: 343px;
  max-width: 100%;
  font-size: var(--font-size-6xl);
  color: var(--color-white);
}

.hotelBrandSymbol {
  width: 962.7px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 0px 94.7px;
  max-width: 100%;
}

.undrawMaleAvatarG98d3Icon {
  align-self: stretch;
  flex: 1;
  position: relative;
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
  z-index: 2;
}

.rectangleShapes {
  height: 137.7px;
  width: 129.3px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 14px 0px 0px;
  box-sizing: border-box;
}

.header {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
  padding: 0px 37.39999999999963px 8.899999999999977px 100px;
  box-sizing: border-box;
  position: relative;
  max-width: 100%;
  gap: var(--gap-xl);
  z-index: 2;
  color: var(--color-saddlebrown-100);
}

.bemVindoA {
  margin: 0;
  position: relative;
  font-size: inherit;
  font-weight: 400;
  font-family: inherit;
  z-index: 1;
}

.hotelaria1 {
  margin: 0;
  align-self: stretch;
  height: 134px;
  position: relative;
  font-size: 154px;
  letter-spacing: 0.07em;
  font-weight: 700;
  font-family: inherit;
  display: inline-block;
  flex-shrink: 0;
  z-index: 1;
  margin-top: -13px;
}

.rectangleShapes2 {
  width: 1091px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  max-width: 100%;
}

.rectangleShapes1 {
  width: 1517px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl) 269px;
  box-sizing: border-box;
  max-width: 100%;
  font-size: 50px;
}

.scroll {
  position: relative;
  letter-spacing: 0.05em;
  white-space: nowrap;
  z-index: 1;
}

.subtraction2Icon {
  height: 60.8px;
  width: 60.6px;
  position: relative;
  z-index: 1;
}

.subtractionVector {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 8px 0px 10.199999999999818px;
}

.scrollParent {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 15.2px 0px;
}

.headerInstance {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  font-size: var(--font-size-6xl);
}

.bemVindo {
  align-self: stretch;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px 38px;
  box-sizing: border-box;
  position: relative;
  gap: 143px;
  max-width: 100%;
}

.quartos2 {
  margin: 0;
  width: 333px;
  position: relative;
  font-size: inherit;
  letter-spacing: 0.05em;
  font-weight: 700;
  font-family: inherit;
  display: inline-block;
}

.atualizarPromocaoInstance {
  width: 1587px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  box-sizing: border-box;
  max-width: 100%;
}

.frameChild {
  align-self: stretch;
  height: 1301px;
  position: relative;
  border-radius: 0px 0px var(--br-mini) var(--br-mini);
  background-color: var(--color-white);
  border: 2px solid var(--color-saddlebrown-100);
  box-sizing: border-box;
  display: none;
}

.devonJanseVanRensburgWedfIcon {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
  object-fit: cover;
  display: none;
}

.frameTriplet {
  position: absolute;
  height: 86.79%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 13.21%;
  left: 0%;
  background-color: var(--color-saddlebrown-200);
  z-index: 1;
}

.frameItem {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  background-color: var(--color-saddlebrown-100);
  display: none;
}

.noiteEstrelada {
  margin: 0;
  position: absolute;
  height: 41.84%;
  width: 38.71%;
  top: 29.08%;
  left: 32.58%;
  font-size: inherit;
  font-weight: 700;
  font-family: inherit;
  display: inline-block;
  z-index: 1;
}

.rectangleGroup {
  position: absolute;
  top: 926px;
  left: 0px;
  background-color: var(--color-saddlebrown-100);
  width: 1599px;
  height: 141px;
  z-index: 2;
}

.frameInner {
  position: absolute;
  top: 869px;
  left: 751px;
  width: 100px;
  height: 20px;
  z-index: 2;
}

.devonJanseVanRensburgWedfParent {
  align-self: stretch;
  height: 1067px;
  position: relative;
  background-image: url("/public/devonjansevanrensburg-wedftzv0quunsplash-1@2x.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: top;
  z-index: 1;
}

.informaesChild {
  height: 51px;
  width: 51px;
  position: relative;
}

.informaes1 {
  align-self: stretch;
  position: relative;
}

.header1 {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-2xs) 0px 0px;
}

.informaes {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 0px 11px;
  z-index: 1;
}

.informaesWrapper {
  height: 60px;
  width: 267px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 6px 0px 0px;
  box-sizing: border-box;
}

.cadastrarPromooChild {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  border-radius: var(--br-12xs);
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
}

.cadastrarPromoo1 {
  position: absolute;
  height: 37.18%;
  width: 79.89%;
  top: 30.77%;
  left: 12.46%;
  font-size: var(--font-size-6xl);
  display: inline-block;
  font-family: var(--font-montserrat);
  color: var(--color-white);
  text-align: left;
  z-index: 1;
}

.cadastrarPromoo {
  height: 78px;
  flex: 1;
  position: relative;
  max-width: 100%;
}

.cadastrarPromooWrapper {
  cursor: pointer;
  border: none;
  padding: 0;
  background-color: transparent;
  width: 353px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  max-width: 100%;
  z-index: 1;
}

.rADailyRateChild {
  position: absolute;
  top: 0px;
  left: 0px;
  border-radius: var(--br-12xs);
  width: 288px;
  height: 78px;
  z-index: 1;
}

.r147Diria {
  position: absolute;
  top: 24px;
  left: 57px;
  font-size: var(--font-size-6xl);
  display: inline-block;
  font-family: var(--font-montserrat);
  color: var(--color-white);
  text-align: left;
  width: 201px;
  height: 29px;
  z-index: 2;
}

.rADailyRate {
  cursor: pointer;
  border: none;
  padding: 0;
  background-color: transparent;
  height: 78px;
  width: 288px;
  position: relative;
}

.rRDiaText {
  width: 1274px;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
  max-width: 100%;
  gap: var(--gap-xl);
}

.rRDiaTextWrapper {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  box-sizing: border-box;
  max-width: 100%;
  text-align: center;
  font-size: var(--font-size-6xl);
  color: var(--color-saddlebrown-100);
}

.rectangleParent {
  width: 1604px;
  border-radius: 0px 0px var(--br-mini) var(--br-mini);
  background-color: var(--color-white);
  border: 2px solid var(--color-saddlebrown-100);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px var(--padding-59xl);
  gap: 79px;
  max-width: 100%;
}

.rectangleDiv {
  align-self: stretch;
  height: 1301px;
  position: relative;
  border-radius: 0px 0px var(--br-mini) var(--br-mini);
  background-color: var(--color-white);
  border: 2px solid var(--color-saddlebrown-100);
  box-sizing: border-box;
  display: none;
}

.maskGroupIcon1 {
  position: absolute;
  right: 0px;
  bottom: -41px;
  width: 1598px;
  height: 967px;
  object-fit: cover;
  z-index: 1;
}

.subRoomFrame {
  position: absolute;
  top: 0px;
  left: 0px;
  background-color: var(--color-saddlebrown-200);
  width: 100%;
  height: 100%;
  z-index: 2;
}

.excluirPromocaoChild {
  position: absolute;
  top: 869px;
  left: 751px;
  width: 100px;
  height: 20px;
  z-index: 3;
}

.excluirPromocao {
  height: 926px;
  flex: 1;
  position: relative;
  max-width: 100%;
}

.atualizarPromocao {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 3px 0px 2px;
  box-sizing: border-box;
  max-width: 100%;
}

.frameChild1 {
  height: 141px;
  width: 1602px;
  position: relative;
  background-color: var(--color-saddlebrown-100);
  display: none;
  max-width: 100%;
}

.noiteEstrelada1 {
  margin: 0;
  height: 59px;
  position: relative;
  font-size: inherit;
  font-weight: 700;
  font-family: inherit;
  display: inline-block;
  z-index: 1;
}

.groupDiv {
  flex: 1;
  background-color: var(--color-saddlebrown-100);
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: var(--padding-22xl) var(--padding-xl) var(--padding-22xl) var(--padding-60xl);
  box-sizing: border-box;
  max-width: 100%;
  z-index: 2;
}

.frameWrapper {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px var(--padding-60xl);
  box-sizing: border-box;
  max-width: 100%;
}

.informaesItem {
  height: 51px;
  width: 51px;
  position: relative;
}

.informaes3 {
  align-self: stretch;
  position: relative;
}

.roomLabel {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-2xs) 0px 0px;
}

.informaes2 {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 0px 11px;
  z-index: 4;
}

.promoText {
  width: 272px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 22px var(--padding-2xs) 0px 0px;
  box-sizing: border-box;
}

.atualizarpromooChild {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  border-radius: var(--br-12xs);
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
}

.atualizarPromoo {
  position: absolute;
  height: 37.18%;
  width: 76.49%;
  top: 30.77%;
  left: 13.31%;
  font-size: var(--font-size-6xl);
  display: inline-block;
  font-family: var(--font-montserrat);
  color: var(--color-white);
  text-align: left;
  z-index: 1;
}

.atualizarpromoo {
  cursor: pointer;
  border: none;
  padding: 0;
  background-color: transparent;
  height: 78px;
  flex: 1;
  position: relative;
  min-width: 229px;
  max-width: 100%;
  z-index: 1;
}

.excluirChild {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
}

.lixeiraDeReciclagem1Icon {
  position: absolute;
  height: 62.96%;
  width: 60%;
  top: 18.52%;
  right: 20%;
  bottom: 18.52%;
  left: 20%;
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
  object-fit: cover;
  z-index: 1;
}

.excluir {
  height: 81px;
  width: 85px;
  position: relative;
  z-index: 1;
}

.updatePromo {
  width: 473px;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: center;
  gap: 0px 35px;
  max-width: 100%;
}

.infoTagChild {
  position: absolute;
  top: 0px;
  left: 0px;
  border-radius: var(--br-12xs);
  width: 288px;
  height: 78px;
  z-index: 1;
}

.r150Diria {
  color: var(--color-white);
  white-space: pre-wrap;
}

.r155R150DiriaContainer {
  position: absolute;
  top: 0px;
  left: 6px;
  display: inline-block;
  width: 265px;
  height: 30px;
  z-index: 2;
}

.deleteTagChild {
  position: absolute;
  top: 16px;
  left: 0px;
  width: 85px;
  height: 3px;
  z-index: 4;
}

.deleteTag {
  position: absolute;
  top: 24px;
  left: 8px;
  width: 271px;
  height: 30px;
}

.infoTag {
  height: 78px;
  width: 288px;
  position: relative;
  text-align: left;
}

.infoFrame {
  width: 1263px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
  max-width: 100%;
  gap: var(--gap-xl);
}

.starBackground {
  width: 1591px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  box-sizing: border-box;
  max-width: 100%;
  text-align: center;
  font-size: var(--font-size-6xl);
  color: var(--color-saddlebrown-100);
}

.rectangleContainer {
  position: absolute;
  top: 0px;
  left: 57px;
  border-radius: 0px 0px var(--br-mini) var(--br-mini);
  background-color: var(--color-white);
  border: 2px solid var(--color-saddlebrown-100);
  box-sizing: border-box;
  width: 1604px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  padding: 0px 0px 75px;
  max-width: 100%;
}

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
}

.frameParent {
  align-self: stretch;
  height: 1302px;
  position: relative;
  max-width: 100%;
}

.frameChild2 {
  align-self: stretch;
  height: 1301px;
  position: relative;
  border-radius: 0px 0px var(--br-mini) var(--br-mini);
  background-color: var(--color-white);
  border: 2px solid var(--color-gray-200);
  box-sizing: border-box;
  display: none;
  z-index: 0;
}

.fredKleberGtbaxavlvsgUnsplaIcon {
  position: absolute;
  bottom: -141px;
  left: -2px;
  width: 1602px;
  height: 1066px;
  object-fit: cover;
  z-index: 1;
}

.imageChild {
  position: absolute;
  top: 0px;
  left: 0px;
  background-color: rgba(20, 39, 74, 0.2);
  width: 100%;
  height: 100%;
  z-index: 2;
}

.imageItem {
  position: absolute;
  top: 869px;
  left: 751px;
  width: 100px;
  height: 20px;
  z-index: 3;
}

.image {
  align-self: stretch;
  height: 926px;
  position: relative;
}

.frameChild3 {
  height: 141px;
  width: 1602px;
  position: relative;
  background-color: var(--color-saddlebrown-100);
  display: none;
  max-width: 100%;
}

.noiteEstrelada2 {
  margin: 0;
  height: 59px;
  width: 639px;
  position: relative;
  font-size: inherit;
  font-weight: 700;
  font-family: inherit;
  display: inline-block;
  flex-shrink: 0;
  max-width: 100%;
  z-index: 1;
}

.rectangleParent2 {
  flex: 1;
  background-color: var(--color-saddlebrown-100);
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-end;
  padding: var(--padding-22xl) 403px;
  box-sizing: border-box;
  max-width: 100%;
  z-index: 2;
}

.group {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px 76px;
  box-sizing: border-box;
  max-width: 100%;
}

.groupIcon {
  width: 51px;
  height: 51px;
  position: absolute;
  margin: 0 !important;
  right: 587px;
  bottom: 88px;
  object-fit: cover;
  z-index: 1;
}

.informaesInner {
  height: 51px;
  width: 51px;
  position: relative;
}

.informaes5 {
  align-self: stretch;
  position: relative;
}

.iNFORMAES {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-2xs) 0px 0px;
}

.informaes4 {
  width: 261px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 0px 11px;
  z-index: 4;
}

.rRDiria {
  height: 61px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 40px 0px 0px;
  box-sizing: border-box;
}

.atualizarpromooItem {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  border-radius: var(--br-12xs);
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
}

.atualizarPromoo3 {
  position: absolute;
  height: 37.18%;
  width: 76.49%;
  top: 30.77%;
  left: 13.31%;
  font-size: var(--font-size-6xl);
  display: inline-block;
  font-family: var(--font-montserrat);
  color: var(--color-white);
  text-align: left;
  z-index: 1;
}

.atualizarpromoo1 {
  cursor: pointer;
  border: none;
  padding: 0;
  background-color: transparent;
  height: 78px;
  flex: 1;
  position: relative;
  min-width: 229px;
  max-width: 100%;
  z-index: 4;
}

.excluirItem {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
}

.lixeiraDeReciclagem1Icon1 {
  position: absolute;
  height: 62.96%;
  width: 60%;
  top: 18.52%;
  right: 20%;
  bottom: 18.52%;
  left: 20%;
  max-width: 100%;
  overflow: hidden;
  max-height: 100%;
  object-fit: cover;
  z-index: 1;
}

.excluir1 {
  height: 81px;
  width: 85px;
  position: relative;
  z-index: 4;
}

.atualizarPromoo2 {
  width: 473px;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: center;
  gap: 0px 35px;
  max-width: 100%;
}

.ratesBoxChild {
  position: absolute;
  top: 0px;
  left: 0px;
  border-radius: var(--br-12xs);
  width: 288px;
  height: 78px;
  z-index: 1;
}

.r150Diria1 {
  color: var(--color-white);
  white-space: pre-wrap;
}

.r155R150DiriaContainer1 {
  position: absolute;
  top: 0px;
  left: 7px;
  display: inline-block;
  width: 268px;
  height: 29px;
  z-index: 2;
}

.lineSeparatorChild {
  position: absolute;
  top: 15px;
  left: 0px;
  width: 85px;
  height: 3px;
  z-index: 4;
}

.lineSeparator {
  position: absolute;
  top: 24px;
  left: 13px;
  width: 275px;
  height: 29px;
}

.ratesBox {
  height: 78px;
  width: 288px;
  position: relative;
  text-align: left;
}

.rectangle {
  width: 1228px;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
  max-width: 100%;
  gap: var(--gap-xl);
}

.atualizarPromoo1 {
  width: 1556px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  box-sizing: border-box;
  max-width: 100%;
  text-align: center;
  font-size: var(--font-size-6xl);
  color: var(--color-saddlebrown-100);
}

.rectangleParent1 {
  position: absolute;
  top: 0px;
  left: 50px;
  border-radius: 0px 0px var(--br-mini) var(--br-mini);
  background-color: var(--color-white);
  border: 2px solid var(--color-gray-200);
  box-sizing: border-box;
  width: 1604px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  padding: 0px 0px var(--padding-59xl);
  max-width: 100%;
}

.tagPromooItem {
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

.rectangleShape {
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

.promoo1 {
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

.tagPromoo1 {
  position: absolute;
  top: 73px;
  left: 0px;
  width: 515px;
  height: 258px;
  z-index: 4;
}

.tag {
  align-self: stretch;
  height: 1302px;
  position: relative;
  max-width: 100%;
}

.rRDiaLine {
  align-self: stretch;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  padding: 0px 0px 12px;
  box-sizing: border-box;
  gap: 81px 0px;
  max-width: 100%;
  text-align: left;
  color: var(--color-white);
}

.pathNavigationChild {
  height: 50px;
  width: 50px;
  position: relative;
  min-height: 50px;
}

.pathNavigationItem {
  height: 50px;
  width: 50px;
  position: relative;
  min-height: 50px;
}

.pathNavigation {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 0px 21px;
}

.groupedFrames {
  width: 1585px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  box-sizing: border-box;
  max-width: 100%;
}

.atualizarPromocaoInstanceParent {
  width: 1661px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  gap: 149px 0px;
  max-width: 100%;
  text-align: center;
  font-size: var(--font-size-41xl);
  color: var(--color-saddlebrown-100);
  font-family: var(--font-montserrat);
}

.noiteEstreladaGroup {
  width: 1861px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl) 271px;
  box-sizing: border-box;
  max-width: 100%;
}

.footer {
  width: 109px;
  position: relative;
  display: inline-block;
  z-index: 1;
}

.textAtFooter {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl) 0px 57px;
  text-align: center;
  font-size: var(--font-size-6xl);
}

.quartos {
  width: 100%;
  position: relative;
  background-color: var(--color-white);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px 114px;
  box-sizing: border-box;
  gap: 148px 0px;
  letter-spacing: normal;
  text-align: left;
  font-size: 24px;
  color: var(--color-white);
  font-family: var(--font-montserrat);
}

@media screen and (max-width: 1250px) {
  .header {
    flex-wrap: wrap;
  }

  .rectangleParent {
    padding-bottom: 51px;
    box-sizing: border-box;
  }

  .infoFrame {
    flex-wrap: wrap;
  }

  .frameParent {
    height: auto;
    min-height: 1302;
  }

  .rectangle {
    flex-wrap: wrap;
  }

  .tag {
    height: auto;
    min-height: 1302;
  }

  .atualizarPromocaoInstanceParent {
    gap: 74px 0px;
  }

  .noiteEstreladaGroup {
    padding-bottom: 74px;
    box-sizing: border-box;
  }
}

@media screen and (max-width: 1100px) {
  .simboloHotelaria {
    flex: 1;
  }

  .hotelBrandSymbol {
    flex-wrap: wrap;
    gap: 0px 47px;
  }

  .header {
    padding-left: 50px;
    box-sizing: border-box;
  }

  .bemVindo {
    gap: 71px;
  }

  .rRDiaText {
    flex-wrap: wrap;
  }

  .quartos {
    gap: 74px 0px;
  }
}

@media screen and (max-width: 750px) {
  .simboloHotelaria {
    min-width: 100%;
  }

  .pginas {
    gap: 21px;
  }

  .promotionTags {
    min-width: 100%;
  }

  .hotelBrandSymbol {
    gap: 0px 24px;
  }

  .header {
    padding-left: 25px;
    box-sizing: border-box;
  }

  .bemVindoA {
    font-size: 40px;
  }

  .hotelaria1 {
    font-size: 62px;
  }

  .bemVindo {
    gap: 36px;
  }

  .quartos2 {
    font-size: var(--font-size-29xl);
  }

  .noiteEstrelada {
    font-size: var(--font-size-29xl);
  }

  .rectangleParent {
    gap: 39px;
    padding-bottom: 33px;
    box-sizing: border-box;
  }

  .noiteEstrelada1 {
    font-size: var(--font-size-29xl);
  }

  .promoo {
    font-size: var(--font-size-29xl);
  }

  .noiteEstrelada2 {
    font-size: var(--font-size-29xl);
  }

  .promoo1 {
    font-size: var(--font-size-29xl);
  }

  .rRDiaLine {
    gap: 40px 0px;
  }

  .atualizarPromocaoInstanceParent {
    gap: 37px 0px;
  }

  .noiteEstreladaGroup {
    padding-bottom: 48px;
    box-sizing: border-box;
  }

  .quartos {
    gap: 37px 0px;
  }
}

@media screen and (max-width: 450px) {
  .hotelaria {
    font-size: 19px;
  }

  .pginas {
    display: none;
  }

  .bemVindoA {
    font-size: 30px;
  }

  .hotelaria1 {
    font-size: 38px;
  }

  .rectangleShapes1 {
    padding-bottom: 175px;
    box-sizing: border-box;
  }

  .scroll {
    font-size: var(--font-size-xl);
  }

  .quartos2 {
    font-size: var(--font-size-17xl);
  }

  .noiteEstrelada {
    font-size: var(--font-size-17xl);
  }

  .informaes1 {
    font-size: var(--font-size-xl);
  }

  .cadastrarPromoo1 {
    font-size: var(--font-size-xl);
  }

  .r147Diria {
    font-size: var(--font-size-xl);
  }

  .rectangleParent {
    gap: var(--gap-xl);
  }

  .noiteEstrelada1 {
    font-size: var(--font-size-17xl);
  }

  .informaes3 {
    font-size: var(--font-size-xl);
  }

  .atualizarPromoo {
    font-size: var(--font-size-xl);
  }

  .updatePromo {
    flex-wrap: wrap;
  }

  .r155R150DiriaContainer {
    font-size: var(--font-size-xl);
  }

  .promoo {
    font-size: var(--font-size-17xl);
  }

  .noiteEstrelada2 {
    font-size: var(--font-size-17xl);
  }

  .informaes5 {
    font-size: var(--font-size-xl);
  }

  .atualizarPromoo3 {
    font-size: var(--font-size-xl);
  }

  .atualizarPromoo2 {
    flex-wrap: wrap;
  }

  .r155R150DiriaContainer1 {
    font-size: var(--font-size-xl);
  }

  .promoo1 {
    font-size: var(--font-size-17xl);
  }

  .rRDiaLine {
    gap: 20px 0px;
  }

  .atualizarPromocaoInstanceParent {
    gap: 19px 0px;
  }

  .footer {
    font-size: var(--font-size-xl);
  }
}
</style>
