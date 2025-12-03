const db = {
    // --- API Calls ---

    saveContact: async function (data) {
        try {
            const response = await fetch('/api/contacts', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving contact:', error);
        }
    },

    getContacts: async function () {
        try {
            const response = await fetch('/api/contacts');
            return await response.json();
        } catch (error) {
            console.error('Error fetching contacts:', error);
            return [];
        }
    },

    clearContacts: async function () {
        await fetch('/api/contacts', { method: 'DELETE' });
    },

    saveDonation: async function (data) {
        try {
            const response = await fetch('/api/donations', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving donation:', error);
        }
    },

    getDonations: async function () {
        try {
            const response = await fetch('/api/donations');
            return await response.json();
        } catch (error) {
            console.error('Error fetching donations:', error);
            return [];
        }
    },

    clearDonations: async function () {
        await fetch('/api/donations', { method: 'DELETE' });
    },

    saveSubscriber: async function (email) {
        try {
            const response = await fetch('/api/subscribers', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: email })
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving subscriber:', error);
        }
    },

    getSubscribers: async function () {
        try {
            const response = await fetch('/api/subscribers');
            return await response.json();
        } catch (error) {
            console.error('Error fetching subscribers:', error);
            return [];
        }
    },

    clearSubscribers: async function () {
        await fetch('/api/subscribers', { method: 'DELETE' });
    },

    getOrders: async function () {
        try {
            const response = await fetch('/api/orders');
            return await response.json();
        } catch (error) {
            console.error('Error fetching orders:', error);
            return [];
        }
    },

    clearOrders: async function () {
        await fetch('/api/orders', { method: 'DELETE' });
    },

    // --- New Methods ---

    saveVolunteer: async function (data) {
        try {
            const response = await fetch('/api/volunteers', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving volunteer:', error);
        }
    },

    getVolunteers: async function () {
        try {
            const response = await fetch('/api/volunteers');
            return await response.json();
        } catch (error) {
            console.error('Error fetching volunteers:', error);
            return [];
        }
    },

    saveBooking: async function (data) {
        try {
            const response = await fetch('/api/bookings', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving booking:', error);
        }
    },

    getBookings: async function () {
        try {
            const response = await fetch('/api/bookings');
            return await response.json();
        } catch (error) {
            console.error('Error fetching bookings:', error);
            return [];
        }
    },

    saveRSVP: async function (data) {
        try {
            const response = await fetch('/api/rsvps', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving RSVP:', error);
        }
    },

    getRSVPs: async function () {
        try {
            const response = await fetch('/api/rsvps');
            return await response.json();
        } catch (error) {
            console.error('Error fetching RSVPs:', error);
            return [];
        }
    }
};

// Expose to window
window.db = db;
