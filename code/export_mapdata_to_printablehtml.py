# jinja2で印刷むけのテンプレートを使い、地図データをHTMLに出力する

template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Printable HTML</title>
  <style>
    body {
      width: 21cm;
      height: 29.7cm;
      margin: 0;
      padding: 0;
      background: white;
      box-sizing: border-box;
    }

    .container {
      padding: 1cm;
    }

    .header, .footer {
      width: 100%;
      text-align: center;
      position: fixed;
    }

    .header {
      top: 0cm;
      border-bottom: 0.1cm solid #000;
    }

    .footer {
      bottom: 0cm;
      border-top: 0.1cm solid #000;
    }

    .content {
      padding: 1cm;
      margin-top: 2cm;
      margin-bottom: 2cm;
      overflow: auto;
    }

    table {
      width: 100%;
    }

    td {
      width: 50%;
      vertical-align: top;
    }

    img {
      max-width: 100%;
      max-height: 100%;
    }

    @page {
      size: A4;
      margin: 0;
    }

    @media print {
      html, body {
        width: 210mm;
        height: 297mm;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h2>印刷物のタイトル</h2>
    </div>

    <div class="content">
      <table>
        <!-- Repeat this block for each row -->
        <tr>
          <td>
            <p>ここに文字情報を入れてください。</p>
          </td>
          <td>
            <img src="your_image.jpg" alt="Image">
          </td>
        </tr>
        <!-- End of repeat -->
      </table>
    </div>

    <div class="footer">
      <p>ここにフッタの情報を入れてください。</p>
    </div>
  </div>
</body>
</html>
"""