
const slideUp =
{
    distance: '150%',
    origin: 'bottom',
    opacity: .2,
    easing: 'ease-in-out'
};

const slideDown =
{
    origin: 'top',
    distance: '120px',
    opacity: null,
    easing: 'ease-in-out',
    opacity: 0.5
};

const item_slide_up = [
    document.querySelector('.headline'),
    document.querySelector('.heading-1')
];

ScrollReveal()
    .reveal(
        item_slide_up, slideUp,
        {
            delay: 200,
            reset: true
        });

const fade_in =
{
    opacity: 0.2,
    easing: 'ease-in-out'
};

