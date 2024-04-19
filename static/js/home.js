function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


function getProducts(categoryId) {
    console.log("Fetching products for category:", categoryId);
    fetch(`/store_app/get-products-by-category/${categoryId}/`)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        const productContainer = document.getElementById('product-container');
        productContainer.innerHTML = ''; // Clear existing content
  
        // Check if data is an array (assuming it directly provides an array of products)
        if (Array.isArray(data)) {
          data.forEach(product => {
            console.log(product.name);
            const productColumn = document.createElement('div');
            productColumn.classList.add('col-lg-4', 'my-2');

            const productElement = document.createElement('div');
            productElement.classList.add('box-element', 'product');

            const productImage = document.createElement('img');
            productImage.classList.add('thumbnail');
            productImage.src = product.imageURL;
            productElement.appendChild(productImage);

            const productName = document.createElement('h6');
            productName.innerHTML = `<strong>${product.name}</strong>`;
            productElement.appendChild(productName);

            const hrElement = document.createElement('hr');
            productElement.appendChild(hrElement);

            const addToCartBtn = document.createElement('button');
            addToCartBtn.classList.add('btn', 'btn-shop', 'btn-outline-primary', 'add-btn');
            addToCartBtn.id = 'product-info';
            addToCartBtn.setAttribute('data-product-id', product.id);
            addToCartBtn.textContent = 'Shop now';
            productElement.appendChild(addToCartBtn);

            const viewBtn = document.createElement('a');
            viewBtn.classList.add('btn', 'btn-outline-success');
            viewBtn.href = '#';
            viewBtn.textContent = 'Details';
            productElement.appendChild(viewBtn);

            const priceElement = document.createElement('h4');
            priceElement.style.display = 'inline-block';
            priceElement.style.float = 'right';
            priceElement.innerHTML = `<strong>$${product.price.toFixed(2)}</strong>`;
            productElement.appendChild(priceElement);

            productColumn.appendChild(productElement);
            productContainer.appendChild(productColumn);

          });
        } else {
          console.error('Products data is not in the expected format');
        }
      })
      .catch(error => console.error(error));
  }

