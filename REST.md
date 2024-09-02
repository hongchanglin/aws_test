You're welcome! Let's break down the difference between a REST API and a non-REST API in simple terms.

### **REST API:**
- **REST** stands for **REpresentational State Transfer**.
- A REST API follows a specific set of rules or guidelines for how you can interact with it.
- **Key Characteristics:**
  - **Uses HTTP Methods:** REST APIs use standard HTTP methods like GET, POST, PUT, DELETE to perform actions.
  - **Stateless:** Each request from a client to the server must contain all the information needed to understand and process the request. The server does not remember anything about the client between requests.
  - **Resource-Based:** Everything in a REST API is treated as a "resource" (like an object or piece of data), and each resource has a unique URL.
  - **Standard Data Formats:** REST APIs often use JSON or XML to exchange data between the client and server.

  **Example:** If you want to get information about a book from a REST API, you might send a GET request to `https://api.books.com/books/123`, where `123` is the ID of the book.

### **Non-REST API:**
- Non-REST APIs don't follow the specific REST guidelines. They can use different rules or protocols to communicate.
- **Examples of Non-REST APIs:**
  - **SOAP (Simple Object Access Protocol):** A protocol that uses XML to exchange information, often with more strict rules than REST.
  - **GraphQL:** A newer approach where clients can request exactly the data they need, and nothing more, in a single request.
  - **RPC (Remote Procedure Call):** A protocol where you execute a function on a remote server, often without worrying about resources or HTTP methods.

  **Example:** In a SOAP API, to get information about the same book, you might send a specially formatted XML request to a specific endpoint, and the server will respond with an XML document.

### **Key Differences:**

- **Structure and Flexibility:**
  - **REST:** More flexible, follows a clear and consistent structure using standard web protocols (like HTTP).
  - **Non-REST:** Can be more rigid (like SOAP) or more flexible in different ways (like GraphQL).

- **Data Format:**
  - **REST:** Typically uses JSON or XML.
  - **Non-REST:** SOAP always uses XML, while others (like GraphQL) might use different formats.

- **Ease of Use:**
  - **REST:** Often simpler and easier to use, especially for web-based applications.
  - **Non-REST:** Can be more complex, but sometimes offers more powerful or specific capabilities.

### **Summary:**
- **REST API** follows a set of guidelines making it easy and consistent to use over the web.
- **Non-REST API** can vary widely in how they work, offering different levels of complexity, power, and flexibility depending on the specific needs.

In essence, REST is like following a recipe with specific steps, while non-REST APIs might give you more freedom or require a different set of instructions to achieve the same goal.

https://hackernoon.com/lang/ja/25-%E3%81%AE%E4%B8%BB%E8%A6%81%E3%81%AA-REST-API-%E9%9D%A2%E6%8E%A5%E3%81%AE%E8%B3%AA%E5%95%8F%E3%81%A8%E5%9B%9E%E7%AD%94

1. REST とは何ですか?
Representational State Transferの略で、フロントエンドや外部システムとの統合を持つアプリケーションを開発するための、HTTPプロトコルに基づくアーキテクチャスタイルです。

REST、REST API、RESTful APIという、3つの用語があります。

2. REST API とは何ですか?
まずはAPI：APIはApplication Programming Interfaceの略。
APIは、個々のアプリケーションが通信してデータを交換できるようにするプログラミングインタフェースです。
REST APIは、RESTの原則に則る（従う）APIで、すべてのデータをソースとして扱い、それぞれが一意のUniform Resource Identifier(URI)で表されます。

3. RESTful API とは何ですか?
REST APIと同じ、用語上の違いです。

4. REST の 2 つの主な原則は何ですか?
REST APIは、次の2つの原則に従う必要があります。
a. クライアントとサーバーの分離：クライアントとサーバー間のやり取りは、リクエストと応答の形式で実行されます。クライアントとのみがリクエストを送信でき、サーバーのみが応答を送信して、互いに独立に動作できます。
b. 単一プロトコル：クライアントとサーバー間のやり取りは、単一のプロトコルを使用して実行する必要があります（HTTPプロトコル）。

5. REST のその他の原則についてご存知ですか?
REST API リクエストはサーバー上に状態を保存せず、サーバーのレイヤーを通過してキャッシュできます。
また、サーバーの応答で実行可能コードをクライアントに送信することもできます。
サーバー ステートレス: サーバーは過去のリクエスト/応答に関する情報を保存しません。各リクエストと応答には、対話を完了するために必要なすべての情報が含まれています。ステートレス通信により、サーバーの負荷が軽減され、メモリが節約され、パフォーマンスが向上します。
階層化システム: クライアントと API サーバーの間に、レイヤーの形で追加のサーバーを配置して、さまざまな機能を実行できます。REST 原則に基づいて構築されたシステムでは、レイヤーはモジュール式であり、クライアントとサーバー間の通信に影響を与えることなく追加および削除できます。
キャッシュ可能性: サーバーの応答は、そのリソースがキャッシュ可能かどうかを示します。これにより、クライアントは任意のリソースをキャッシュしてパフォーマンスを向上させることができます。オンデマンド コード: サーバーは、クライアント アプリケーション内で実行するために、応答でクライアントに実行可能コードを送信できます。

6. リソースとは何ですか?
RESTでは、サーバー側でアクセス可能なすべてのオブジェクトがリソースとして指定されます。リソースとは、タイプ、関連付けられたデータ、サーバー上の他のリソースとの関係、及びリソースを操作するために使用できるメソードのリストを持つオブジェクトのことです。例えば、リソースには、HTMLまたはテキストファイル、データファイル、画像、またはビデオ、実行可能なコードファイルなど。
リソースは、Uniform Resource Identifierによって識別されます。クライアントは、HTTP要求でURIを使用してリソースにアクセスします。


7. URLとは何ですか?
http://yasuda:pass@www.example.com:8080/news/index.htm?page=2&msg=yes#hot

http:はスキーム

yasuda:pass＠はユーザー情報

www.example.comはホスト

:8080はポスト

/news/index.htmはパス：指定したオーソリティの中でのアクセス先を指定します。
httpでは、公開領域内でのディレクトリ名とファイル名

?page=2&msg=yesはクエリ：パスの中でさらにアクセス内容を細かく識別します。httpでは、サーバー上で動作するプログラムへの指示や命令が書かれることが多いです。

#hot フラグメント
サーバーから送られた情報をクライアント（ブラウザ）が処理する際に使います。

8. CRUD とは何ですか?
作成　Create: POST
取得　Request: GET
更新　Update: PUT
削除　Delete: DELETE

9. サーバー応答のペイロードとは何を意味しますか?
Payload
クライアントによって要求されたリソースデータを指します。
HTTP応答ペイロードとも呼ばれます。
サーバーが提供する内容に応じて、JSON、XML、HTML、画像、ファイルなどになります。

10. REST メッセージングとは何ですか?
RESTにおけるメッセージングとは、クライアントとサーバーの間のメッセージ交換を指します。通信は常に、クライアントからサーバーに対してHTTP要求を行うことから始まります。サーバーはこの要求を処理し、要求のステータスとクライアントが要求したリソースを示すHTTP応答を返します。（ステータス　+　リソース）


11. REST のメッセージ ブローカーとは何ですか?

12. REST ではどのような HTTP リクエスト メソッドがサポートされていますか?

13. POST メソッドと PUT メソッドの違いは何ですか?

14. HTTP リクエストの主な部分は何ですか?

15. HTTP 応答の主な部分は何ですか?

16. HTTPサーバーの応答が成功した場合のコードを少なくとも3つ挙げてください。

17. リクエストをリダイレクトするときに、少なくとも 4 つのサーバー HTTP 応答コードを指定します。

18. HTTP サーバー応答が失敗した場合のコードを少なくとも 4 つ挙げてください。

19. 少なくとも 3 つのサーバー エラー コードを挙げてください。

20. RESTとGraphQLの違いは何ですか？

21. REST と SOAP の違いは何ですか?

22. REST と AJAX の違いは何ですか?

23. REST API 開発における「コントラクト ファースト」アプローチとは何ですか?

24. Contract First の利点は何ですか?

25. REST API 開発に対するコードファースト アプローチとは何ですか?