window.openMarathonModal = function (bookType) {
    // Open the modal
    openModal('marathon-modal');

    // Reset form first
    const form = document.getElementById('marathon-form');
    form.reset();

    // Pre-fill based on selection
    if (bookType) {
        const inputMap = {
            'english': 'qty_gita_english',
            'hindi': 'qty_gita_hindi',
            'marathi': 'qty_gita_marathi'
        };

        const inputName = inputMap[bookType];
        if (inputName) {
            const input = form.querySelector(`input[name="${inputName}"]`);
            if (input) input.value = 1;
        }
    }
};

window.handleMarathonSubmit = async function (event) {

    event.preventDefault();
    const form = event.target;
    const btn = form.querySelector('button[type="submit"]');
    const successMsg = document.getElementById('booking-success');

    // Gather data
    const name = form.querySelector('input[name="name"]').value;
    const phone = form.querySelector('input[name="phone"]').value;
    const email = form.querySelector('input[name="email"]').value;

    const qtyGitaEng = parseInt(form.querySelector('input[name="qty_gita_english"]').value) || 0;
    const qtyGitaHin = parseInt(form.querySelector('input[name="qty_gita_hindi"]').value) || 0;
    const qtyGitaMar = parseInt(form.querySelector('input[name="qty_gita_marathi"]').value) || 0;


    if (qtyGitaEng === 0 && qtyGitaHin === 0 && qtyGitaMar === 0) {
        alert('Please select at least one book.');
        return;
    }

    const books = [];
    if (qtyGitaEng > 0) books.push(`Gita English (${qtyGitaEng})`);
    if (qtyGitaHin > 0) books.push(`Gita Hindi (${qtyGitaHin})`);
    if (qtyGitaMar > 0) books.push(`Gita Marathi (${qtyGitaMar})`);


    const totalQty = qtyGitaEng + qtyGitaHin + qtyGitaMar;
    const booksSummary = books.join(', ');

    // Disable button
    btn.disabled = true;
    btn.textContent = 'Booking...';

    try {
        const response = await fetch('/api/book-marathon', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name,
                phone,
                email,
                books_summary: booksSummary,
                total_qty: totalQty
            })
        });

        const result = await response.json();

        if (result.status === 'success') {
            successMsg.style.display = 'block';
            form.reset();
            setTimeout(() => {
                closeModal();
                successMsg.style.display = 'none';
                btn.disabled = false;
                btn.textContent = 'Confirm Booking';
                alert('Booking Confirmed! Please collect your books from the Mandir.');
            }, 2000);
        } else {
            alert('Error: ' + result.error);
            btn.disabled = false;
            btn.textContent = 'Confirm Booking';
        }
    } catch (error) {
        console.error('Error submitting booking:', error);
        alert('Failed to submit booking. Please try again.');
        btn.disabled = false;
        btn.textContent = 'Confirm Booking';
    }
};
