document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('artworkModal');
    const closeModal = document.getElementById('closeModal');

    function showModal() {
        modal.style.display = 'flex';
        setTimeout(() => modal.classList.add('show'), 10);
        document.body.style.overflow = 'hidden';
    }

    function hideModal() {
        modal.classList.remove('show');
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
        document.body.style.overflow = 'auto';
    }

    if (closeModal) {
        closeModal.addEventListener('click', hideModal);
    }

    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                hideModal();
            }
        });
    }

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            hideModal();
        }
    });

    document.querySelectorAll('.artwork-card').forEach(function(card) {
        card.addEventListener('click', function() {
            const title = card.dataset.title;
            const artist = card.dataset.artist;
            const year = card.dataset.year;
            const medium = card.dataset.medium;
            const dimensions = card.dataset.dimensions;
            const description = card.dataset.description;
            const image = card.dataset.image;

            document.getElementById('modalImage').src = image;
            document.getElementById('modalTitle').textContent = title;
            document.getElementById('modalArtist').textContent = artist;
            document.getElementById('modalYear').textContent = year;
            document.getElementById('modalMedium').textContent = medium;
            document.getElementById('modalDimensions').textContent = dimensions;
            document.getElementById('modalDescription').textContent = description;

            showModal();
        });
    });
});