var summ = 0;
$("td").each(function() {
  summ += Number($(this).text());
});;
console.log("Result: " + summ);