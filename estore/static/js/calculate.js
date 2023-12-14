        // Retrieve values from Django template variables
        const cartTotal = parseFloat(document.getElementById('cartTotal').innerText);
        const taxTotal = parseFloat(document.getElementById('taxTotal').innerText);

        let taxRate;

        // Calculate tax based on different total ranges
        if (cartTotal < 50) {
            taxRate = 0.1; // 10% tax
        } else if (cartTotal < 100) {
            taxRate = 0.05; // 5% tax
        } else {
            taxRate = 0.025; // 2.5% tax
        }

        // Calculate tax amount
        const calculatedTax = cartTotal * taxRate;

        // Calculate the grand total including tax
        const grandTotal = cartTotal + calculatedTax;

        // Update the Tax and Grand Total elements with the calculated values
        document.getElementById('taxTotal').innerText = calculatedTax.toFixed(2);
        document.getElementById('grandTotal').innerText = grandTotal.toFixed(2);