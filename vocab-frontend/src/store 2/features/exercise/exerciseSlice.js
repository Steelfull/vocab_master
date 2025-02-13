import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  currentExercise: null,
  currentItemIndex: 0,
  loading: false,
  error: null,
  progress: {
    correctAnswers: 0,
    totalAttempts: 0
  }
};

const exerciseSlice = createSlice({
  name: 'exercise',
  initialState,
  reducers: {
    startLoading(state) {
      state.loading = true;
      state.error = null;
    },
    setExercise(state, action) {
      state.currentExercise = action.payload;
      state.currentItemIndex = 0;
      state.loading = false;
    },
    nextItem(state) {
      state.currentItemIndex += 1;
    },
    recordAnswer(state, action) {
      state.progress.totalAttempts += 1;
      if (action.payload) state.progress.correctAnswers += 1;
    },
    setError(state, action) {
      state.error = action.payload;
      state.loading = false;
    }
  }
});

export const { 
  startLoading, 
  setExercise, 
  nextItem, 
  recordAnswer, 
  setError 
} = exerciseSlice.actions;

export default exerciseSlice.reducer;