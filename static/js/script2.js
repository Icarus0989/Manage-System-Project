window.onload = () => {
    new Vue({
        el: '#app',
        data: {
            list: ['pure', 'xyz', 'abc'],
            selectedItem: 'Select an option'
        },
        methods: {
            select(item) {
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
                        default: () => []
                    },
                    defaultText: {
                        type: String,
                        default: 'Select an option'
                    }
                },
                data() {
                    return {
                        selectItem: this.defaultText,
                        showSelect: false,
                        selectListHeight: 0
                    };
                },
                mounted() {
                    this.selectListContent = this.$refs.selectListContent;
                    this.selectListHeight = this.selectListContent.offsetHeight;
                    this.selectListContent.style.height = '0';
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
    });
};
