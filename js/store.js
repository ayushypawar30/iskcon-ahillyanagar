const products = [
    {
        id: 1,
        name: "Bhagavad Gita As It Is",
        category: "Books",
        price: 250,
        image: "images/prabhupada.png" // Local placeholder
    },
    {
        id: 2,
        name: "Srimad Bhagavatam Set (18 Vols)",
        category: "Books",
        price: 7500,
        image: "images/prabhupada.png" // Local placeholder
    },
    {
        id: 3,
        name: "Krsna: The Supreme Personality of Godhead",
        category: "Books",
        price: 450,
        image: "images/prabhupada.png" // Local placeholder
    },
    {
        id: 4,
        name: "The Nectar of Devotion",
        category: "Books",
        price: 300,
        image: "images/prabhupada.png" // Local placeholder
    },
    {
        id: 5,
        name: "Tulsi Mala (108 Beads)",
        category: "Devotional",
        price: 150,
        image: "images/puja.png" // Local placeholder
    },
    {
        id: 6,
        name: "Saffron Japa Bag",
        category: "Devotional",
        price: 100,
        image: "images/puja.png" // Local placeholder
    },
    {
        id: 7,
        name: "Cotton Dhoti Kurta Set",
        category: "Clothing",
        price: 800,
        image: "images/temple_hall.png" // Local placeholder
    },
    {
        id: 8,
        name: "Premium Incense Sticks (Sandalwood)",
        category: "Devotional",
        price: 120,
        image: "images/puja.png" // Local placeholder
    }
];

function renderProducts() {
    const grid = document.getElementById('product-grid');
    if (!grid) return;

    grid.innerHTML = products.map(product => `
        <div class="timing-card" style="text-align: center;">
            <img src="${product.image}" alt="${product.name}" onerror="this.onerror=null; this.src='images/placeholder.png';" style="width: 100%; height: 200px; object-fit: cover; border-radius: 5px; margin-bottom: 10px;">
            <h3>${product.name}</h3>
            <p style="color: var(--primary-color); font-weight: bold;">₹${product.price}</p>
            <button class="btn" onclick="addToCart(${product.id})" style="margin-top: 10px;">Add to Cart</button>
        </div>
    `).join('');
}

function addToCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const product = products.find(p => p.id === productId);

    const existingItem = cart.find(item => item.id === productId);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ ...product, quantity: 1 });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    alert(`${product.name} added to cart!`);
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const count = cart.reduce((total, item) => total + item.quantity, 0);
    const badge = document.getElementById('cart-count');
    if (badge) badge.textContent = count;
}

function renderCart() {
    const cartContainer = document.getElementById('cart-items');
    const totalElement = document.getElementById('cart-total');
    if (!cartContainer) return;

    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    if (cart.length === 0) {
        cartContainer.innerHTML = '<p>Your cart is empty.</p>';
        totalElement.textContent = '0';
        return;
    }

    cartContainer.innerHTML = cart.map(item => `
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #eee;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <img src="${item.image}" style="width: 50px; height: 50px; object-fit: cover;">
                <div>
                    <h4>${item.name}</h4>
                    <p>₹${item.price} x ${item.quantity}</p>
                </div>
            </div>
            <button onclick="removeFromCart(${item.id})" style="color: red; background: none; border: none; cursor: pointer;"><i class="fas fa-trash"></i></button>
        </div>
    `).join('');

    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    totalElement.textContent = total;
}

function removeFromCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(item => item.id !== productId);
    localStorage.setItem('cart', JSON.stringify(cart));
    renderCart();
    updateCartCount();
}

document.addEventListener('DOMContentLoaded', () => {
    renderProducts();
    updateCartCount();
    renderCart();
});
