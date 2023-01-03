const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#cupcake-form")


async function getAllCupcakes() {
    const allCupcakes = await axios.get('/api/cupcakes');
    $cupcakeList.empty();
    for (let cupcake of allCupcakes.data.cupcakes){
        const $cupcake = $(
            `<li id=${cupcake.id}>
                Flavor: ${cupcake.flavor} Size: ${cupcake.size} Rating: ${cupcake.rating}
                <div>
                    <img src=${cupcake.image} height="300">
                </div>
            </li> 
        `);
    $cupcakeList.append($cupcake);
    }
};


$cupcakeForm.on("click", "#add-cupcake", async function(evt){
    // evt.preventDefault();
    form = $cupcakeForm[0]
    await axios.post('/api/cupcakes', {flavor: form[1].value, size: form[2].value, rating: form[3].value, image: form[4].value })
});

getAllCupcakes();
