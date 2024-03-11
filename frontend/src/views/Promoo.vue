<template>
  <div :class="$style.promoo">
    <div :class="$style.promooChild" />
    <div :class="$style.promooItem" />
    <div :class="$style.promooInner">
      <div :class="$style.vectorParent">
        <img :class="$style.frameChild" alt="" />
        <div :class="$style.hotelariaWrapper">
          <b :class="$style.hotelaria">HOTELARIA</b>
        </div>
      </div>
    </div>
    <div :class="$style.rectangleParent">
      <div :class="$style.frameItem" />
      <h1 :class="$style.noiteEstrelada" ref="quartoCometaRef">Quarto cometa</h1>
    </div>
    <div :class="$style.lineDiv" />
    <div :class="$style.home">Home</div>
    <b :class="$style.quartos">Quartos</b>
    <div :class="$style.perfil">Perfil</div>
    <img :class="$style.union3Icon" alt="" src="../assets/promotions/union-3.svg" />
    <main :class="$style.selectionBox">
      <section :class="$style.backgroundImage">
        <div :class="$style.devonJanseVanRensburgWedfParent">
          <img :class="$style.devonJanseVanRensburgWedfIcon" loading="lazy" alt=""
            src="../assets/promotions/devonjansevanrensburg-wedftzv0quunsplash-1@2x.png" />
          <div :class="$style.frameWrapper">
            <div :class="$style.rParent">
              <div :class="$style.r">
                <div :class="$style.r14701">{{ oldValue }}</div>
              </div>
              <div :class="$style.r">
                <div :class="$style.r14700">R$ {{ reservationValue }}</div>
              </div>
              <div :class="$style.seleovalor">
                <div :class="$style.footerFrame">
                  <div :class="$style.valueFrameParent">
                    <input :class="$style.valueFrame" type="text" v-model="discountValue" />
                    <div :class="$style.frameParent">
                      <div :class="$style.valorWrapper">
                        <div :class="$style.valor">Valor</div>
                      </div>
                      <div :class="$style.div">*</div>
                    </div>
                    <div :class="$style.digiteOValorParaSerDesconWrapper">
                      <div :class="$style.digiteOValor" ref="valorDigitado" @click="inputClick">
                        Digite o valor para ser descontado
                      </div>
                    </div>
                  </div>
                </div>
                <button :class="$style.cancelar">
                  <div :class="$style.cancelarInner">
                    <div :class="$style.vectorGroup" @click="onGroupContainerClick">
                      <img :class="$style.frameInner" alt="" src="../assets/promotions/rectangle-1090.svg" />
                      <RouterLink to="/rooms-page" :class="$style.cancelar1">Cancelar</RouterLink>
                    </div>
                  </div>
                </button>
                <button :class="$style.seleovalorInner">
                  <div :class="$style.frameContainer">
                    <div :class="$style.vectorContainer" @click="confirmClick">
                      <img :class="$style.rectangleIcon" alt="" src="../assets/promotions/rectangle-1090-1.svg" />
                      <b :class="$style.confirmar">Confirmar</b>
                    </div>
                  </div>
                </button>
              </div>
              <span :class="$style.errorMsg">{{ errorMsg }}</span>
            </div>
          </div>
        </div>
        <div :class="$style.footerText">
          <b :class="$style.footer">FOOTER</b>
        </div>
      </section>
    </main>
  </div>
</template>
<script lang="ts">
import { defineComponent, ref } from "vue";
import { useApiService, PromotionModel, PromotionUpdateModel } from '../services/apiService';
import { useRouter } from 'vue-router';
import { RouterLink } from 'vue-router';

const reservationValue = ref<string>('');

const { getPromotion, createPromotion, getRoomId, updatePromotion, getCurrentPromotion } = useApiService();

export default defineComponent({
  name: "Promoo-Page",
  data() {
    return {
      reservationValue: '',
      oldValue: '',
      mostrarOldValue: false,
      errorMsg: ''
    };
  },
  async mounted() {
    try {
      const quartoCometaElement = this.$refs.quartoCometaRef.innerText.toLowerCase();
      const room_id = this.$route.params.id;
      const promotion = (await getPromotion(room_id)).data.data;
      if (promotion) {
        this.reservationValue = promotion.newValue;
        this.oldValue = `R$ ${promotion.reservationValue}`;
      } else {
        const price = (await getRoomId(quartoCometaElement)).data.data.price
        this.reservationValue = price;
      }

    } catch (error) {
      console.error("Erro ao verificar promoção durante o mounted:", error);
    }
    return {
      reservationValue
    }
  },
  methods: {
    onGroupContainerClick() {
      // Please sync "Quartos 2" to the project
    },
    inputClick() {
      this.$refs.valorDigitado.innerText = ''
    }
    ,
    async confirmClick() {
      const room_id = this.$route.params.id;
      const promotion = (await getPromotion(room_id)).data.data;
      console.log('promotion')
      if (promotion) {
        const currentDiscount = (await getCurrentPromotion(room_id)).data.data
        const promotioUpdateData: PromotionUpdateModel = {
          user: "Pedro",
          adm_key: "879456",
          room_id: this.$route.params.id,
          currentDiscountValue: currentDiscount.currentValue,
          newDiscountValue: this.discountValue
        };

        const promotionUpdate = (await updatePromotion(promotioUpdateData)).data.data;
        console.log(promotionUpdate)
        if (promotionUpdate) {
          alert('Atualizado')
        } else {
          this.errorMsg = 'Valor de desconto inválido'
        }

        return {
          promotionCreate
        }
      } else {
        const promotionData: PromotionModel = {
          user: "Pedro",
          adm_key: "879456",
          hotel: "noite estrelada",
          room_id: this.$route.params.id,
          reservationValue: this.reservationValue,
          discountValue: this.discountValue
        };

        const promotionCreate = (await createPromotion(promotionData)).data.data;
        if (promotionCreate) {
          alert('Cadastrado')
        } else {
          this.errorMsg = 'Valor de desconto inválido'
        }

        return {
          promotionCreate
        }
      }
    },
    onGroupContainer2Click() {
      // Please sync "Quartos 2" to the project
    },
  },
});
</script>
<style module>
.promooChild {
  align-self: stretch;
  height: 465px;
  position: relative;
  background-color: var(--color-saddlebrown-100);
  flex-shrink: 0;
  display: none;
  z-index: 0;
}

.errorMsg {
  color: var(--color-error);
  margin-top: -20%;
  font-size: var(--font-size-5xl);
}

.promooItem {
  align-self: stretch;
  height: 465px;
  position: relative;
  background-color: var(--color-saddlebrown-100);
  flex-shrink: 0;
  display: none;
  z-index: 1;
}

.frameChild {
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
  top: 0%;
  left: 0%;
  letter-spacing: 0.15em;
  display: inline-block;
  width: 100%;
  height: 100%;
}

.hotelariaWrapper {
  position: absolute;
  height: 19.46%;
  width: 68.75%;
  top: 39.6%;
  right: 15.63%;
  bottom: 40.94%;
  left: 15.63%;
}

.vectorParent {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0%;
  right: 0%;
  bottom: 0%;
  left: 0%;
}

.promooInner {
  width: 256px;
  height: 149px;
  position: relative;
  flex-shrink: 0;
  display: none;
  z-index: 4;
  font-size: var(--font-size-5xl);
  color: var(--color-saddlebrown-100);
}

.frameItem {
  height: 465px;
  width: 1920px;
  position: relative;
  background-color: var(--color-saddlebrown-100);
  display: none;
  max-width: 100%;
}

.noiteEstrelada {
  margin: 0;
  width: 639px;
  position: relative;
  font-size: inherit;
  font-weight: 700;
  font-family: inherit;
  display: inline-block;
  max-width: 100%;
  z-index: 3;
}

.rectangleParent {
  align-self: stretch;
  background-color: var(--color-saddlebrown-100);
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: center;
  padding: 109px var(--padding-xl);
  box-sizing: border-box;
  min-height: 465px;
  max-width: 100%;
  z-index: 2;
  font-size: 80px;
}

.lineDiv {
  width: 98px;
  height: 2px;
  position: relative;
  border-top: 2px solid var(--color-white);
  box-sizing: border-box;
  flex-shrink: 0;
  display: none;
  z-index: 4;
}

.home {
  width: 78px;
  position: relative;
  display: none;
  text-shadow: 0.5px 0 0 #fff, 0 0.5px 0 #fff, -0.5px 0 0 #fff,
    0 -0.5px 0 #fff;
  z-index: 5;
}

.quartos {
  width: 105px;
  position: relative;
  display: none;
  z-index: 6;
}

.perfil {
  width: 66px;
  position: relative;
  display: none;
  text-shadow: 0.5px 0 0 #fff, 0 0.5px 0 #fff, -0.5px 0 0 #fff,
    0 -0.5px 0 #fff;
  z-index: 7;
}

.union3Icon {
  width: 100%;
  height: 321px;
  position: absolute;
  margin: 0 !important;
  right: 0px;
  bottom: 0px;
  left: 0px;
  max-width: 100%;
  overflow: hidden;
  flex-shrink: 0;
}

.devonJanseVanRensburgWedfIcon {
  align-self: stretch;
  height: 769px;
  position: relative;
  max-width: 100%;
  overflow: hidden;
  flex-shrink: 0;
  object-fit: cover;
}

.r14700 {
  height: 104px;
  width: 338px;
  position: relative;
  font-weight: 900;
  display: inline-block;
  flex-shrink: 0;
  white-space: nowrap;
  max-width: 100%;
}

.r14701 {
  height: 104px;
  width: 338px;
  margin-bottom: -50%;
  position: relative;
  font-weight: 900;
  display: inline-block;
  flex-shrink: 0;
  white-space: nowrap;
  max-width: 100%;
  text-decoration: line-through;
}

.r {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-end;
  padding: 0px 48px;
  box-sizing: border-box;
  max-width: 100%;
}

.valueFrame {
  border: 2px solid rgba(20, 39, 74, 0.5);
  outline: none;
  background-color: var(--color-white);
  width: 100%;
  height: 78px;
  position: absolute;
  margin: 0 !important;
  right: 0px;
  bottom: 0px;
  left: 0px;
  box-sizing: border-box;
}

.valor {
  position: relative;
  text-shadow: 0.3px 0 0 #8b4513, 0 0.3px 0 #8b4513, -0.3px 0 0 #8b4513,
    0 -0.3px 0 #8b4513;
}

.valorWrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 9px 0px 0px;
}

.div {
  position: relative;
  font-weight: 900;
  color: #d2691e;
}

.frameParent {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
}

.digiteOValor {
  height: 27px;
  flex: 1;
  position: relative;
  display: inline-block;
  z-index: 1;
}

.digiteOValorParaSerDesconWrapper {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px 0px 16px;
  font-size: 16px;
  color: #cecece;
  font-family: var(--font-inter);
}

.valueFrameParent {
  align-self: stretch;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px 25px;
  position: relative;
  gap: 33px;
}

.footerFrame {
  width: 318px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 8px 0px 0px;
  box-sizing: border-box;
}

.frameInner {
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

.cancelar1 {
  position: absolute;
  height: 37.18%;
  width: 64.55%;
  top: 30.77%;
  left: 17.99%;
  font-size: var(--font-size-6xl);
  display: inline-block;
  font-family: var(--font-montserrat);
  color: var(--color-white);
  text-align: left;
  z-index: 1;
}

.vectorGroup {
  height: 78px;
  flex: 1;
  position: relative;
  cursor: pointer;
}

.cancelarInner {
  flex: 1;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
}

.cancelar {
  cursor: pointer;
  border: none;
  padding: 0;
  background-color: transparent;
  width: 189px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
}

.rectangleIcon {
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

.confirmar {
  position: absolute;
  height: 37.18%;
  width: 75.13%;
  top: 30.77%;
  left: 13.23%;
  font-size: var(--font-size-6xl);
  display: inline-block;
  font-family: var(--font-montserrat);
  color: var(--color-white);
  text-align: left;
  z-index: 1;
}

.vectorContainer {
  height: 78px;
  flex: 1;
  position: relative;
  cursor: pointer;
}

.frameContainer {
  flex: 1;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
}

.seleovalorInner {
  cursor: pointer;
  border: none;
  padding: 0;
  background-color: transparent;
  width: 189px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
}

.seleovalor {
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: flex-start;
  padding: 0px 0px 0px 0px;
  gap: 0px 28px;
  font-size: var(--font-size-6xl);
}

.rParent {
  width: 579px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 130px 0px;
  max-width: 100%;
}

.frameWrapper {
  width: 989px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  box-sizing: border-box;
  max-width: 100%;
}

.devonJanseVanRensburgWedfParent {
  align-self: stretch;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 57px 0px;
  max-width: 100%;
}

.footer {
  width: 109px;
  position: relative;
  display: inline-block;
  z-index: 1;
}

.footerText {
  width: 1123px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  box-sizing: border-box;
  max-width: 100%;
  text-align: center;
  font-size: var(--font-size-6xl);
  color: var(--color-white);
}

.backgroundImage {
  width: 1155px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  gap: 729px 0px;
  max-width: 100%;
  text-align: left;
  font-size: 64px;
  color: var(--color-saddlebrown-100);
  font-family: var(--font-montserrat);
}

.selectionBox {
  width: 1887px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  padding: 0px var(--padding-xl);
  box-sizing: border-box;
  max-width: 100%;
}

.promoo {
  width: 100%;
  position: relative;
  background-color: var(--color-white);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px 100px;
  box-sizing: border-box;
  gap: 130px 0px;
  letter-spacing: normal;
  text-align: left;
  font-size: var(--font-size-6xl);
  color: var(--color-white);
  font-family: var(--font-montserrat);
}

@media screen and (max-width: 1125px) {
  .backgroundImage {
    gap: 364px 0px;
  }
}

@media screen and (max-width: 1050px) {
  .noiteEstrelada {
    font-size: 40px;
  }

  .r14700 {
    font-size: 51px;
  }

  .seleovalor {
    flex-wrap: wrap;
  }

  .promoo {
    gap: 65px 0px;
  }
}

@media screen and (max-width: 750px) {
  .rParent {
    gap: 65px 0px;
  }

  .devonJanseVanRensburgWedfParent {
    gap: 28px 0px;
  }

  .backgroundImage {
    gap: 182px 0px;
  }

  .promoo {
    gap: 32px 0px;
  }
}

@media screen and (max-width: 450px) {
  .hotelaria {
    font-size: 19px;
  }

  .noiteEstrelada {
    font-size: var(--font-size-5xl);
  }

  .home {
    font-size: var(--font-size-xl);
  }

  .quartos {
    font-size: var(--font-size-xl);
  }

  .perfil {
    font-size: var(--font-size-xl);
  }

  .r14700 {
    font-size: 38px;
  }

  .r {
    padding-left: var(--padding-xl);
    padding-right: var(--padding-xl);
    box-sizing: border-box;
  }

  .valor {
    font-size: var(--font-size-xl);
  }

  .div {
    font-size: var(--font-size-xl);
  }

  .valueFrameParent {
    gap: 16px;
  }

  .cancelar1 {
    font-size: var(--font-size-xl);
  }

  .confirmar {
    font-size: var(--font-size-xl);
  }

  .rParent {
    gap: 32px 0px;
  }

  .footer {
    font-size: var(--font-size-xl);
  }

  .backgroundImage {
    gap: 91px 0px;
  }
}
</style>
