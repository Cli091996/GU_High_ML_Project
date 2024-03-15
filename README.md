# GU_High_ML_Project
to be updated

# Check if selected_order_type is 'All' or a specific order type
    if selected_order_type == 'All':
        for order in unique_order_types:
            # Ensure that boolean indexing doesn't result in empty arrays
            idx = np.where(order_type == order)[0]
            if idx.size > 0:
                axs.scatter(actual[idx], predicted[idx], alpha=0.5, color=color_dict[order], label=order)
                axs.vlines(actual[idx], predicted[idx], actual[idx], color=color_dict[order], alpha=0.7, linewidth=0.5)
    else:
        idx = np.where(order_type == selected_order_type)[0]
        if idx.size > 0:
            axs.scatter(actual[idx], predicted[idx], alpha=0.5, color=color_dict[selected_order_type], label=selected_order_type)
            axs.vlines(actual[idx], predicted[idx], actual[idx], color=color_dict[selected_order_type], alpha=0.7, linewidth=0.5)
    

# To edit 
#%%html
<script>
document.addEventListener("DOMContentLoaded", function() {
    document.addEventListener('mouseup', function(event) {
        var selection = window.getSelection().toString();
        if(selection.trim() !== '') {
            var cells = document.querySelectorAll('.jp-CodeCell');
            cells.forEach(function(cell) {
                var textNodes = cell.querySelectorAll('.CodeMirror-line span');
                textNodes.forEach(function(node) {
                    var text = node.textContent.trim();
                    if(text === selection) {
                        node.style.background = 'red'; // Change to suit
                    }
                });
            });
        }
    });
});
</script>
