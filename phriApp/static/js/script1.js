window.onload = () => {
    const app = new Vue({
        el: '#app',
        data: {
            list: ['Salim Yusuf', 'Hertzel Gerstein', 'PJ Devereaux', 'Emilie Cote','Sanjit']
        },
        methods: {
            select(item) {
                // alert(item);
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