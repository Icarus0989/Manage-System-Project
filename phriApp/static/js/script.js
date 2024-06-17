window.onload = () => {
    const app = new Vue({
        el: '#app',
        data: {
            list: ['PHRI', 'WHRI', 'McMaster', 'HHS']
        },
        methods: {
            select(item) {
                console.log('Selected item:', item);
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
                        default: 'Organizations'
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
                    // Access the DOM element
                    this.selectListContent = this.$refs.selectListContent;
                    // Measure its height
                    this.selectListHeight = this.selectListContent.offsetHeight;
                    // Initially hide the element
                    this.selectListContent.style.height = '0';
                },
                methods: {
                    showSelectList() {
                        this.showSelect = !this.showSelect;
                        // Toggle the height to show or hide the content
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
