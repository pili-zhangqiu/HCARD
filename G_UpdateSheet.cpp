Chilkat C/C++ Library Downloads
MS Visual C/C++

Linux/CentOS C/C++

Alpine Linux C/C++

MAC OS X C/C++

armhf/aarch64 C/C++

C++ Builder

iOS C/C++

Android C/C++

Win Mobile 5.0/Pocket PC 2003

Solaris C/C++

FreeBSD C/C++

OpenBSD C/C++

MinGW C/C++

#include <CkJsonObject.h>
#include <CkHttp.h>
#include <CkHttpResponse.h>

void ChilkatSample(void)
    {
    //  This example requires the Chilkat API to have been previously unlocked.
    //  See Global Unlock Sample for sample code.

    //  This example uses a previously obtained access token having permission for the
    //  Google Sheets scope.

    //  In this example, Get Google Sheets OAuth2 Access Token, the access
    //  token was saved to a JSON file.  This example fetches the access token from the file..
    CkJsonObject jsonToken;
    bool success = jsonToken.LoadFile("qa_data/tokens/googleSheets.json");
    if (jsonToken.HasMember("access_token") == false) {
        std::cout << "No access token found." << "\r\n";
        return;
    }

    CkHttp http;
    http.put_AuthToken(jsonToken.stringOf("access_token"));

    //  First get the cells in the range A1:B5
    http.SetUrlVar("range","Sheet1!A1:B5");
    http.SetUrlVar("spreadsheetId","1_SO2L-Y6nCayNpNppJLF0r9yHB2UnaCleGCKeE4O0SA");
    const char *jsonResponse = http.quickGetStr("https://sheets.googleapis.com/v4/spreadsheets/{$spreadsheetId}/values/{$range}");
    if (http.get_LastMethodSuccess() != true) {
        std::cout << http.lastErrorText() << "\r\n";
        return;
    }

    std::cout << jsonResponse << "\r\n";

    CkJsonObject json;
    json.put_EmitCompact(false);
    json.Load(jsonResponse);

    //  A sample response is shown below.

    //  {
    //    "range": "Sheet1!A1:B5",
    //    "majorDimension": "ROWS",
    //    "values": [
    //      [
    //        "Item",
    //        "Cost"
    //      ],
    //      [
    //        "Wheel",
    //        "$20.50"
    //      ],
    //      [
    //        "Door",
    //        "$15"
    //      ],
    //      [
    //        "Engine",
    //        "$100"
    //      ],
    //      [
    //        "Totals",
    //        "$135.50"
    //      ]
    //    ]
    //  }

    //  We're going to change the cost of the Engine to $120, and the Totals to $155.50

    json.put_I(3);
    json.put_J(1);
    json.UpdateString("values[i][j]","$120");
    json.put_I(4);
    json.UpdateString("values[i][j]","$155.50");

    //  Show the updated JSON.
    std::cout << json.emit() << "\r\n";

    //  --------------------------------------------------------
    //  Note: This example requires Chilkat v9.5.0.76 or greater.
    //  --------------------------------------------------------

    //  Update the Google Sheet using a PUT request.
    json.put_EmitCompact(true);
    const char *urlToUpdate = "https://sheets.googleapis.com/v4/spreadsheets/{$spreadsheetId}/values/{$range}?valueInputOption=USER_ENTERED";
    const char *xyz = http.quickGetStr(urlToUpdate);
    CkHttpResponse *resp = http.PText("PUT",urlToUpdate,json.emit(),"utf-8","application/json",false,false);
    if (http.get_LastMethodSuccess() != true) {
        std::cout << http.lastErrorText() << "\r\n";
        return;
    }

    //  Examine the response..
    std::cout << "response status code = " << resp->get_StatusCode() << "\r\n";
    std::cout << "response body:" << "\r\n";
    std::cout << resp->bodyStr() << "\r\n";

    //  A sample response body:

    //  {
    //    "spreadsheetId": "1_SO2L-Y6nCayNpNppJLF0r9yHB2UnaCleGCKeE4O0SA",
    //    "updatedRange": "Sheet1!A1:B5",
    //    "updatedRows": 5,
    //    "updatedColumns": 2,
    //    "updatedCells": 10
    //  }

    delete resp;
    }
