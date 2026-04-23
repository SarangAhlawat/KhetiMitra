export const fadeIn = {

  initial: {
    opacity: 0,
    y: 40
  },

  animate: {
    opacity: 1,
    y: 0
  },

  transition: {
    duration: 0.5
  }

};

export const slideInLeft = {

  initial: {
    opacity: 0,
    x: -50
  },

  animate: {
    opacity: 1,
    x: 0
  },

  transition: {
    duration: 0.5
  }

};

export const scaleHover = {

  whileHover: {
    scale: 1.05
  }

};

export const buttonTap = {

  whileTap: {
    scale: 0.95
  }

};