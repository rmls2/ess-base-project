<template>
    <div :class="$style.removePoppupOverlay">
        <div :class="$style.desejaRemover">
            <section :class="$style.removePromotion" />
            <div :class="$style.desejaRemoverPromoo">Deseja remover promoção?</div>
            <div :class="$style.childFrames">
                <div :class="$style.frameWithButtons">
                    <div :class="$style.cancelar" @click="onCancelarTextClick">
                        <RouterLink to="/rooms-page" :class="$style.cancelarBtn">cancelar</RouterLink>
                        <span :class="$style.span"> </span>
                    </div>
                    <RouterLink to="/rooms-page" :class="$style.confirmar" @click="onConfirmarTextClick">
                        confirmar
                    </RouterLink>
                </div>
            </div>
        </div>
    </div>

</template>
<script lang="ts">
import { defineComponent } from "vue";
import { RouterLink } from 'vue-router';
import { useApiService, PromotionModel, PromotionUpdateModel } from '../services/apiService';

export default defineComponent({
    name: "DesejaRemover",
    methods: {
        onCancelarTextClick() {
            // Please sync "Quartos 2" to the project
        },
        async onConfirmarTextClick() {
            const { deletePromotion } = useApiService();
            try{
                const room_id = this.$route.params.id;
                const promotion = await deletePromotion(room_id);
                alert(promotion.data.data.count)
            } catch (error) {
                console.error("Erro ao verificar promoção durante o mounted:", error);
            }

        },
    },
});
</script>
<style module>

.removePoppupOverlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.95); /* Fundo semi-transparente */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999; /* Valor alto para ficar no topo da pilha de camadas */
}

.removePromotion {
    width: 100%;
    height: 100%;
    position: relative;
    margin: 0 !important;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    background-color: var(--color-white);
    z-index: 9999;
}

.cancelarBtn {
    color: var(--color-saddlebrown-100);
}

.confirmarBtn{
    color: var(--color-gray-100);
}

.desejaRemoverPromoo {
    width: 1088px;
    height: 59px;
    position: relative;
    font-weight: 500;
    display: inline-block;
    flex-shrink: 0;
    max-width: 100%;
    z-index: 3;
}

.span {
    color: #000;
}

.cancelar {
    position: relative;
    font-weight: 500;
    cursor: pointer;
    z-index: 1;
}

.confirmar {
    position: relative;
    font-weight: 500;
    color: #8f9779;
    cursor: pointer;
    z-index: 1;
}

.frameWithButtons {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 0px 47px;
    max-width: 100%;
}

.childFrames {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px 9px;
    box-sizing: border-box;
    max-width: 100%;
    color: #8b4513;
}

.desejaRemover {
    width: 28%;
    background-color: var(--color-white);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 101px 70px 56px;
    box-sizing: border-box;
    position: relative;
    gap: 292px 0px;
    letter-spacing: normal;
    text-align: left;
    font-size: var(--font-size-5xl);
    color: #afafaf;
    font-family: var(--font-montserrat);
    z-index: 3;
}

@media screen and (max-width: 750px) {
    .desejaRemoverPromoo {
        font-size: var(--font-size-29xl);
    }

    .cancelar {
        font-size: var(--font-size-29xl);
    }

    .confirmar {
        font-size: var(--font-size-29xl);
    }

    .frameWithButtons {
        flex-wrap: wrap;
    }
}

@media screen and (max-width: 675px) {
    .frameWithButtons {
        gap: 0px 23px;
    }

    .desejaRemover {
        gap: 146px 0px;
        padding-left: var(--padding-16xl);
        padding-right: var(--padding-16xl);
        box-sizing: border-box;
    }
}

@media screen and (max-width: 450px) {
    .desejaRemoverPromoo {
        font-size: var(--font-size-17xl);
    }

    .cancelar {
        font-size: var(--font-size-17xl);
    }

    .confirmar {
        font-size: var(--font-size-17xl);
    }

    .desejaRemover {
        gap: 73px 0px;
    }
}
</style>