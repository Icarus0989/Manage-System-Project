window.onload = () => {
    const app = new Vue({
        el: '#app',
        data: {
            list: ['Government', 'Non-For-Profit organization','For Profit organization'],
            selectedItem: 'LEVEL 2'
        },
        methods: {
            select(item) {
                this.selectedItem = item;
            },
            navigate() {
                if (this.selectedItem === 'Government') {
                    window.location.href = '';
                } else if (this.selectedItem === 'Non-For-Profit organization') {
                    window.location.href = '';
                }
                else if (this.selectedItem === 'For Profit organization') {
                    window.location.href = '';
                }
            }
        },
        components: {
            'select-list': {
                template: '#select-list',
                props: {
                    list: {
                        type: Array,
                        default: () => []
                    },
                    default: {
                        type: String,
                        default: 'LEVEL 2'
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
                    const selectListContent = this.$refs.selectListContent;
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
                        this.hideSelectList();
                    }
                }
            }
        }
    });
};
