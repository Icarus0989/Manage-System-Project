window.onload = () => {
    const app = new Vue({
        el: '#app',
        data: {
            list: ['','','','','','','','','','','']
        },
        created() {
                    fetch('/get_pis')
                        .then(response => response.json())
                        .then(data => {
                            
                            this.list = data;
                            console.log('Fetched data:', this.list); 
                        });
                },
        methods: {
            select(item) {
                 alert(item);
                 this.selectedItem = item;
                document.getElementById('selectedItem').value = item;
            }
        },
        components: {
            'select-list': {
                template: '#select-list',
                props: {
                    list: {
                        type: Array,
                        default: []
                    },
                    default: {
                        type: String,
                        default: 'PI Names'
                    }
                },
                data() {
                    return {
                        selectItem: this.default,
                        showSelect: false,
                        selectListHeight: 0
                    }
                },
                mounted() {
                    selectListContent = this.$refs.selectListContent;
                    this.selectListHeight = selectListContent.offsetHeight;
                    selectListContent.style.height = '0';
                },
                methods: {
                    showSelectList() {
                        this.showSelect = !this.showSelect;
                        this.$refs.selectListContent.style.height = this.showSelect ? this.selectListHeight + 'px' : '0';
                    },
                    hideSelectList() {
                        this.showSelect = false;
                        this.$refs.selectListContent.style.height = '0';
                    },
                    select(item) {
                        this.selectItem = item;
                        this.$emit('select', item);
                    }
                }
            }
        }
    })
}
