$(document).ready(function(){
    var clicked = false;

    $(".cell").click(function(){
        clicked = true;
        var num = 0;
        //alert(this.id);
        let strnum = $("#" + this.id).text();
        if(strnum === ""){
          strnum = 1;
        }
        else if(strnum === "9"){
          strnum = "";
        }
        else{
          num = parseInt(strnum)
          num = num + 1;
          strnum = num.toString();
        }
        $("#" + this.id).text(strnum);
    });
    
        
    $("button").click(function(){
        var counter = 1;
        var sudokulines = [];

        for (let i = 0; i < 9; i++) {
          var line = "";
          for(let j = 0; j < 9; j++){
            let digit = $("#entry" + counter.toString()).text();
            if(digit === ""){
              digit = "0";
            }
            $("#entry" + counter.toString()).fadeOut(500);
            line = line + digit;
            counter = counter + 1;
          }
          sudokulines.push(line);
        }
        
        $("#title").text("solving please wait...");

        $.get("(web address of API)/api?first=" + sudokulines[0] + "&second=" + sudokulines[1] + "&third=" + sudokulines[2] + "&fourth=" + sudokulines[3] + "&fifth=" + sudokulines[4] + "&sixth=" + sudokulines[5] + "&seventh=" + sudokulines[6] + "&eighth=" + sudokulines[7] + "&ninth=" + sudokulines[8], function(data, status){
           jsondata = JSON.parse(JSON.stringify(data));
           const sudokurows = [jsondata['first'].toString(),jsondata['second'].toString(),jsondata['third'].toString(),jsondata['fourth'].toString(),jsondata['fifth'].toString(),jsondata['sixth'].toString(),jsondata['seventh'].toString(),jsondata['eighth'].toString(),jsondata['ninth'].toString()]

           var cellnum = 1;
           for(let m = 0; m < 9; m++){
              const rownums = sudokurows[m].split("");
              for(let n = 0; n < 9; n++){
                  $("#entry" + cellnum.toString()).fadeIn(500);
                  $("#entry" + cellnum.toString()).text(rownums[n].toString());
                  cellnum = cellnum + 1
              }
           }
           $("#title").text("You Successfully Cheated!");
           $(".solvebtn").text(";)");
           $(".solvebtn").hide(1000);
        });   
    });
   
});
