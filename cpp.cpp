#include <Rcpp.h>
#include <iostream>
#include <fstream>

using namespace Rcpp;


NumericVector timesTwo(NumericVector x) {
#include <xlnt/xlnt.hpp>
#include <iostream>
  
  int main() {
    xlnt::workbook wb;
    wb.load("MSFT.xlsx");
    
    auto ws = wb.active_sheet();
    
    std::cout << ws.cell("Open").value().to_string() << std::endl;
    
    return 0;
  }
}




/*** R
timesTwo(33)
*/
