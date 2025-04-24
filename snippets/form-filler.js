function formHelper() {
    var i = 1
    while (i <=9) {
        a = document.getElementsByName(q${i})
        a[0].checked = true
        i = i + 1
    }

    document.forms['feedback_form'].submit()
}
