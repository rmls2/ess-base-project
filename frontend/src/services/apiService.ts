// apiService.ts

import axios, { AxiosResponse } from 'axios';

export interface PromotionModel {
  user: string,
  adm_key: string,
  hotel: string,
  room_id: string,
  reservationValue: number,
  discountValue: number
}


export interface PromotionUpdateModel {
  user: string,
  adm_key: string,
  room_id: string,
  currentDiscountValue: number,
  newDiscountValue: number
}

export function useApiService() {
  const baseUrl = 'http://127.0.0.1:8000'; // Replace with your API URL

  async function getPromotion(room_id: string) {
    try {
      const response = await axios.get(`${baseUrl}/promotions/${room_id}`);
      return response;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
  }

  async function getCurrentPromotion(room_id: string) {
    try {
      const response = await axios.get(`${baseUrl}/promotions/${room_id}/current`);
      return response;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
  }

  async function getRoomId(room_name: string) {
    try {
      const response = await axios.get(`${baseUrl}/promotions/hotel/${room_name}/879456`);
      return response;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
  }

  async function createPromotion(promotionData: PromotionModel): Promise<AxiosResponse> {
    try {
      const response = await axios.post(`${baseUrl}/promotions/register`, promotionData);
      return response;
    } catch (error) {
      console.error('Error creating promotion:', error);
      throw error;
    }
  }

  async function updatePromotion(promotionData: PromotionUpdateModel): Promise<AxiosResponse> {
    try {
      const response = await axios.put(`${baseUrl}/promotions/update`, promotionData);
      return response;
    } catch (error) {
      console.error('Error updating promotion:', error);
      throw error;
    }
  }

  async function deletePromotion(): Promise<AxiosResponse> {
    try {
      const response = await axios.delete(`${baseUrl}/promotions/delete/879456/womrjatajDEa1X0as0W7lVVa`);
      return response;
    } catch (error) {
      console.error('Error deleting promotion:', error);
      throw error;
    }
  }

  return {
    getPromotion,
    getCurrentPromotion,
    getRoomId,
    createPromotion,
    updatePromotion,
    deletePromotion
  };
}
