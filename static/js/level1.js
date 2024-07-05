window.onload = () => {
    const app = new Vue({
        el: '#app',
        data: {
            list: ['Revenue', 'Expense'],
            selectedItem: 'LEVEL 1'
        },
        methods: {
            select(item) {
                this.selectedItem = item;
            },
            navigate() {
                if (this.selectedItem === 'Revenue') {
                    window.location.href = 'tableG.html';
                } else if (this.selectedItem === 'Expense') {
                    window.location.href = 'tableS.html';
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
                        default: 'LEVEL 1'
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