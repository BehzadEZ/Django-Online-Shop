fetch('/api/cart-items')
    .then(response => response.json())
    .then(data => {
        let productList = document.querySelector('.product-list-widget');
        let totalPrice = 0;

        data.cart_items.forEach(item => {
            totalPrice += item.price * item.quantity;
            productList.innerHTML += `
                <li>
                    <div class="product-item">
                        <span class="product-name">${item.name}</span>
                        <span class="product-price">${item.price} تومان</span>
                        <span class="product-quantity">تعداد: ${item.quantity}</span>
                    </div>
                </li>
            `;
        });

        document.querySelector('.price-cart').innerText = totalPrice + ' تومان';
        document.querySelector('.count-cart').innerText = data.cart_items.length;
    });
