def recommedn(budget):
    if budget <= 50000:
        return{
            "cpu": "Ryzen 5 5600",
            "gpu": "RX 6600",
            "ram": "16GB DDR4"
        }
    elif budget <=80000:
        return{
            "cpu": "Intel i5-12400F",
            "gpu": "RX 7600",
            "ram": "16GB DDR4"
        }
    else:
        return{
            "cpu": "Ryzen 7 5700X",
            "gpu": "RTX 4060",
            "ram": "32GB DDR4"
        }