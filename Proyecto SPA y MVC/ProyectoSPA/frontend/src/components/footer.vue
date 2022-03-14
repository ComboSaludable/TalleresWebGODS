<template>

  
    <div>
        <footer>
            <center>
                 Sigue nuestro contenido en GitHub :), LINK: https://github.com/ComboSaludable
            </center>
           
        </footer>
    </div>


</template>

<style scoped>
footer {
    position: fixed;
    height: 40px;
    bottom: 0;
    width: 100%;
    background-color: black;
    color:blue;
}
</style>


<script>


export default({
    name: 'Footer',
    props: [
        'infoFooter'
    ]
})
</script>
