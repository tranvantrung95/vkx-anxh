# Bài toán BA khai thác kho dữ liệu an sinh xã hội — làm việc với VNPT-IT

Ngày lập: 22/10/2026. Trạng thái: dự thảo để trao đổi, chưa được khách hàng xác nhận.

Nguồn: các ý người dùng cung cấp trong cuộc trò chuyện ngày 22/10/2026, bao gồm phần làm rõ sau buổi làm việc với VNPT-IT. Người dùng xác nhận VNPT-IT đã có kho dữ liệu; trong cuộc trò chuyện này chưa cung cấp dữ liệu mẫu, cấu trúc hoặc quyền truy cập kho để phân tích. Tài liệu này không phải biên bản trích xuất từ file quay màn hình.

## 1. Những thông tin hiện có

- Người dùng làm việc với đơn vị VNPT-IT và đảm nhiệm vai trò BA trong dự án.
- VNPT-IT đã có kho dữ liệu về các nhóm đối tượng của các tỉnh/đơn vị liên quan. Chưa xác nhận kho bao phủ những tỉnh, đơn vị, nhóm và thời kỳ cụ thể nào.
- Module có liên quan tới dữ liệu an sinh xã hội, “dân sự” của các tỉnh. Nghĩa và phạm vi của “dân sự” chưa rõ; chưa đồng nhất thuật ngữ này với dân cư hay hộ tịch.
- Nhiệm vụ BA là đọc hiểu, phân tích và tổng hợp dữ liệu đang có: dữ liệu mô tả điều gì, có ý nghĩa nghiệp vụ gì, có thể liên kết và dùng vào những việc gì; từ đó đề xuất các hướng khai thác.
- Vai trò BA được kỳ vọng hiểu sâu về data warehouse và lakehouse để khảo sát kho hiện hữu. Công nghệ được nêu trong lời đề nghị hợp tác: Angular cho frontend, Java Spring Boot cho backend và Oracle cho CSDL; kiến trúc kho, phiên bản và công nghệ từng nguồn thành phần cần xác nhận.
- Các nhóm được nhắc đến: người khuyết tật, thương binh, hoàn cảnh khó khăn, hộ nghèo, thuộc diện chính sách, vùng miền. “Trẻ em” được người dùng nêu kèm dấu hỏi, cần xác nhận có thuộc phạm vi không.
- Cuộc trò chuyện chưa có dữ liệu mẫu, danh mục bảng/nguồn, mô tả hệ thống, danh sách người dùng hoặc đầu ra được thống nhất. Điều này không có nghĩa là phía VNPT-IT chưa có các tài liệu đó.

## 2. Phát biểu bài toán đề xuất

Khảo sát kho dữ liệu hiện hữu của VNPT-IT để mô tả dữ liệu đang phản ánh những đối tượng, sự kiện và trạng thái nghiệp vụ nào; đánh giá độ tin cậy, phạm vi bao phủ và khả năng liên kết; đối chiếu với nhu cầu của đơn vị sử dụng để đề xuất các hướng khai thác có giá trị và khả thi.

Chuỗi công việc chính: **Dữ liệu đang có → ý nghĩa nghiệp vụ → chất lượng và khả năng liên kết → câu hỏi có thể trả lời → người sử dụng và hành động → sản phẩm dữ liệu đề xuất**.

Đây là cách diễn giải phạm vi để thảo luận. Đầu ra có thể phục vụ báo cáo quản lý, tra cứu, đối soát hoặc theo dõi chính sách, tùy dữ liệu thực tế và nhu cầu được xác nhận. Chưa có yêu cầu xây mới hoặc thay thế kho dữ liệu.

## 3. Phạm vi công việc BA đề xuất

| Công việc | Câu hỏi BA cần trả lời | Đầu ra dự kiến |
|---|---|---|
| Kiểm kê kho hiện hữu | Có những bảng/tập dữ liệu nào? Thuộc nguồn, địa bàn và thời kỳ nào? Đang ở lớp thô hay đã chuẩn hóa? | Danh mục dữ liệu, phạm vi bao phủ, sơ đồ luồng và đầu mối xác nhận |
| Đọc hiểu nghiệp vụ | Mỗi dòng đại diện cho ai/việc gì? Các trường, mã, trạng thái và mốc thời gian có nghĩa gì? | Hồ sơ từng bộ dữ liệu, từ điển nghiệp vụ, mô hình quan hệ |
| Đánh giá dữ liệu sau khi được cung cấp | Có đủ, mới, nhất quán và nối được giữa các nguồn không? Nội dung nào cần chủ nguồn xác minh độ đúng? | Báo cáo chất lượng, kết quả thử liên kết và giới hạn sử dụng |
| Đối chiếu nhu cầu sử dụng | Ai có thể dùng? Đang gặp vấn đề gì? Kết quả giúp quyết định hoặc hành động gì? | Các nhu cầu được xác nhận và mức ưu tiên |
| Đề xuất cách khai thác | Câu hỏi nào trả lời được? Cần bổ sung hoặc làm sạch những gì? | Ma trận dữ liệu–ứng dụng, bằng chứng khả thi và phụ thuộc |
| Đặc tả cho đội triển khai | Nhận, nối, chuẩn hóa, cập nhật và cung cấp dữ liệu như thế nào? | Mapping dữ liệu, quy tắc xử lý, phân quyền, tiêu chí nghiệm thu |

BA tự khảo sát và xử lý mẫu dữ liệu, đồng thời cần chủ nguồn/nghiệp vụ xác nhận ý nghĩa. Đầu mối kỹ thuật phối hợp xác định luồng tích hợp và kiến trúc; việc bố trí người phát triển dữ liệu trong giai đoạn triển khai cần được chốt riêng, không giả định có data engineer làm thay BA trong tuần khảo sát.

## 4. Những khái niệm cần làm rõ khi khảo sát kho

### Đơn vị thống kê và quan hệ giữa các đối tượng

Mô hình khảo sát ban đầu có thể gồm: cá nhân, hộ, quan hệ thành viên hộ, nhóm chính sách, hồ sơ/quyết định, chương trình hỗ trợ, lần chi trả hoặc dịch vụ, địa bàn và thời gian. Đây là danh sách để kiểm tra với khách hàng, chưa xác nhận dữ liệu có đủ các đối tượng đó.

Một cá nhân có thể đồng thời thuộc nhiều nhóm; các nhóm không mặc định loại trừ nhau. Phải phân biệt số người duy nhất, số hộ, số hồ sơ, số lượt hưởng và số lần chi trả. Nhận nhiều chính sách không tự động đồng nghĩa với hưởng trùng sai quy định.

“Hoàn cảnh khó khăn” và “thuộc diện chính sách” cần định nghĩa, nguồn xác nhận và thời gian hiệu lực. “Hộ nghèo” cần được tách khỏi thuộc tính cá nhân; nếu phân tích người thuộc hộ nghèo thì phải có quan hệ thành viên hộ hợp lệ tại thời điểm thống kê.

### Liên kết và lịch sử

- Xác nhận mã định danh nào thực sự có và được phép dùng; không mặc định mọi người đều có cùng một mã ở mọi nguồn.
- Xác nhận cách xử lý thiếu mã, sai mã, mã chỉ duy nhất trong một địa phương, thay đổi hộ hoặc địa chỉ. Trường hợp ghép hồ sơ không chắc chắn cần được đưa ra rà soát.
- Phân biệt ngày tiếp nhận dữ liệu, ngày cập nhật, ngày quyết định và khoảng thời gian hiệu lực nghiệp vụ.
- Làm rõ báo cáo lịch sử dùng địa bàn và tiêu chuẩn tại thời điểm đó hay quy đổi theo hiện tại. Danh mục địa bàn và quy tắc phân loại cần có phiên bản khi thay đổi.

### Phạm vi truy cập

Với dữ liệu cá nhân và các nhóm dễ bị tổn thương được nhắc đến, cần hỏi rõ ai được xem hồ sơ định danh, ai chỉ xem số tổng hợp, phạm vi địa bàn, quyền xuất dữ liệu và mục đích sử dụng. Giai đoạn khảo sát có thể bắt đầu bằng cấu trúc dữ liệu và mẫu đã che thông tin định danh.

## 5. Các hướng phân tích và sử dụng dữ liệu để thảo luận

Tất cả các mục dưới đây là đề xuất khảo sát, chưa phải yêu cầu đã chốt hoặc kết luận có thể triển khai.

| Hướng khai thác | Câu hỏi minh họa | Điều kiện dữ liệu cần kiểm tra |
|---|---|---|
| Tổng hợp đối tượng | Có bao nhiêu người/hộ thuộc từng nhóm tại từng địa bàn và thời điểm? | Định nghĩa nhóm, khóa nhận diện, thời gian hiệu lực, độ bao phủ nguồn |
| Phân tích giao nhau | Bao nhiêu người khuyết tật là thành viên hộ nghèo tại thời điểm báo cáo? | Liên kết cá nhân–hộ–nhóm, lịch sử và quy tắc khử trùng |
| Theo dõi biến động | Số đối tượng tăng/giảm do phát sinh thực tế, điều chỉnh hồ sơ hay thay đổi nguồn? | Lịch sử, lý do thay đổi và thông tin đợt nạp dữ liệu |
| Theo dõi hỗ trợ | Đối tượng nào đã được phê duyệt và đã nhận hỗ trợ trong kỳ? | Hồ sơ, quyết định, chi trả/dịch vụ và khóa liên kết |
| Rà soát độ bao phủ | Trong danh sách đủ điều kiện đã được xác nhận, ai chưa có ghi nhận hỗ trợ? | Danh sách đủ điều kiện đầy đủ, dữ liệu hỗ trợ đủ phạm vi và mốc chốt thống nhất |
| Đối soát chất lượng | Những hồ sơ nào thiếu, mâu thuẫn hoặc có khả năng trùng? | Quy tắc kiểm tra, nguồn ưu tiên và quy trình xác minh |

Không có bản ghi trong một nguồn chưa đủ kết luận một người chưa được hỗ trợ. So sánh tỷ lệ giữa địa bàn cần mẫu số phù hợp, cùng định nghĩa và cùng kỳ. Dữ liệu mô tả đơn thuần chưa đủ để kết luận tác động nhân quả của một chính sách.

## 6. BA cần hiểu data warehouse/lakehouse ở mức nào?

Ở mức khái niệm, data warehouse thường tổ chức dữ liệu phục vụ phân tích và báo cáo với định nghĩa thống nhất; lakehouse kết hợp lưu trữ linh hoạt của data lake với khả năng quản lý và truy vấn bảng phục vụ phân tích. Ví dụ, [hướng dẫn Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-lakehouse-warehouse) phân biệt hai lựa chọn theo loại dữ liệu và cách phát triển; đó là ví dụ theo sản phẩm, không phải khuyến nghị chọn Fabric cho dự án này.

Với bối cảnh VNPT-IT đã có kho, BA cần xác định dữ liệu mình được xem thuộc lớp nào, đã qua những quy tắc xử lý gì, còn giữ mức chi tiết và lịch sử nào, có các tập dữ liệu/chỉ tiêu dùng chung nào. Không mặc định dữ liệu nằm trong kho đã sạch hoặc đủ cho mọi phân tích. Đánh giá thay đổi kiến trúc chỉ đặt ra nếu khảo sát phát hiện khoảng trống liên quan đến mục tiêu khai thác.

Các kiến thức BA nên nắm để làm việc với đội dữ liệu:

- Luồng dữ liệu: nguồn → tiếp nhận → chuẩn hóa/tích hợp → tập dữ liệu nghiệp vụ → báo cáo hoặc dịch vụ khai thác.
- ETL/ELT, nạp toàn bộ hay phần thay đổi, lịch cập nhật, dữ liệu đến muộn và cơ chế xử lý lỗi.
- Grain: một dòng dữ liệu đại diện cho cái gì; fact/dimension; khóa định danh và quan hệ nhiều–nhiều.
- Quản lý lịch sử: khi nào giữ giá trị cũ, khi nào cập nhật giá trị hiện tại. SCD Type 2 là một cách lưu phiên bản chiều dữ liệu, không thay thế việc xác định đúng lịch sử nghiệp vụ cần có. Xem [hướng dẫn mô hình chiều của Microsoft](https://learn.microsoft.com/en-us/fabric/data-warehouse/dimensional-modeling-dimension-tables).
- Data quality, metadata, lineage: dữ liệu đủ tin cậy không, trường có nghĩa gì và số liệu được tạo từ nguồn/quy tắc nào.
- Định nghĩa chỉ tiêu: công thức, đơn vị, kỳ, bộ lọc, mẫu số, cách xử lý thiếu và đếm trùng.

Ví dụ câu BA cần đặc tả: “Số người thuộc nhóm X tại ngày chốt T được đếm theo khóa nào, từ quyết định còn hiệu lực nào, theo địa bàn nào; hồ sơ thiếu hoặc mâu thuẫn được xử lý ra sao?”

## 7. Câu hỏi cho buổi khảo sát tiếp theo

1. Đơn vị nào đặt hàng, đơn vị nào sở hữu dữ liệu và ai sẽ dùng kết quả hàng ngày?
2. Ba câu hỏi hoặc quyết định quan trọng nhất họ muốn giải quyết là gì? Hiện tại họ làm thế nào và vướng ở đâu?
3. “Dân sự” cụ thể chỉ lĩnh vực nào? Trẻ em có thuộc phạm vi không? Những nhóm chính sách nào được ưu tiên?
4. Phạm vi địa bàn, khoảng thời gian dữ liệu và giai đoạn triển khai đầu tiên là gì?
5. Kho hiện có những bảng/view/tập dữ liệu nào? Có data dictionary, sơ đồ quan hệ, mô tả nguồn, pipeline và mẫu đã che định danh không?
6. Các nguồn đang dùng mã cá nhân, mã hộ và mã địa bàn nào? Có thể liên kết và giữ lịch sử không?
7. Khách hàng cần báo cáo, dashboard, tra cứu hồ sơ, đối soát, API hay xử lý nghiệp vụ? Xin ví dụ đầu ra cụ thể.
8. Quy tắc phân loại đối tượng và tính chỉ tiêu do ai xác nhận? Có biểu mẫu hoặc tài liệu nghiệp vụ đang áp dụng không?
9. Với nền tảng Angular, Java Spring Boot và Oracle đã nêu, phiên bản và kiến trúc triển khai cụ thể là gì? Các luồng tích hợp nào có sẵn, cần sửa hoặc xây mới? Ranh giới trách nhiệm BA, phát triển và test của mỗi bên là gì?
10. Tần suất cập nhật, thời hạn bàn giao, giới hạn truy cập và cách nghiệm thu được kỳ vọng ra sao?

## 8. Tài liệu nên xin và bước tiếp theo

Ưu tiên xin danh mục bảng/view của kho, mô tả trường và mã, sơ đồ quan hệ, nguồn và thời điểm cập nhật, một báo cáo đang dùng nếu có, cùng mẫu đã che định danh của một nhóm đối tượng. Cần có đầu mối kỹ thuật giải thích dữ liệu và đầu mối nghiệp vụ xác nhận ý nghĩa.

- [x] Ghi lại thông tin ban đầu và cập nhật bối cảnh VNPT-IT đã có kho dữ liệu.
- [x] Chuẩn bị câu hỏi khảo sát và các hướng khai thác có điều kiện dữ liệu đi kèm.
- [ ] Xác nhận bên liên quan, mục tiêu và phạm vi giai đoạn đầu với khách hàng.
- [ ] Nhận danh mục/cấu trúc/mẫu dữ liệu của kho; chọn một nhóm đối tượng để khảo sát từ đầu đến cuối.
- [ ] Thực hiện profiling và lập hồ sơ bộ dữ liệu cùng kết quả thử liên kết.
- [ ] Chọn một tình huống ưu tiên, lập định nghĩa chỉ tiêu và mapping nguồn.
- [ ] Dùng kết quả khảo sát để viết BRD/đặc tả dữ liệu và tiêu chí nghiệm thu tương ứng.

Chưa có dữ liệu trong cuộc trò chuyện để kiểm tra tính khả thi, chất lượng hoặc mức độ bao phủ của kho hiện hữu. Các bước khảo sát chưa hoàn tất không được xem là yêu cầu đã được duyệt.

## 9. Mẫu hồ sơ đánh giá một bộ dữ liệu

Dùng một hồ sơ cho mỗi tập dữ liệu có ý nghĩa nghiệp vụ; không chỉ liệt kê tên cột kỹ thuật.

| Nội dung | Cần ghi nhận |
|---|---|
| Nhận diện và nguồn gốc | Tên bộ dữ liệu; bảng/view; đơn vị cung cấp; đầu mối; nguồn trước khi vào kho |
| Dữ liệu nói về gì | Đối tượng/sự kiện/trạng thái được ghi nhận; quy trình tạo ra bản ghi; ý nghĩa của từng trạng thái |
| Một dòng là gì | Một người, một hộ, một quyết định, một lần hỗ trợ hay một bản chụp theo kỳ; khóa duy nhất kỳ vọng |
| Phạm vi | Tỉnh/đơn vị, nhóm đối tượng, thời kỳ; điều kiện đưa vào và loại ra; phần chưa bao phủ |
| Nội dung và quy tắc | Trường, kiểu dữ liệu, đơn vị đo, mã danh mục, trường bắt buộc, ngày hiệu lực và ngày cập nhật |
| Khả năng liên kết | Khóa nối với tập khác; quan hệ một–một/một–nhiều/nhiều–nhiều; kết quả thử nối và nguy cơ nhân bản |
| Chất lượng đo được | Số dòng, tỷ lệ thiếu ở trường thiết yếu, trùng khóa, mã không hợp lệ, độ mới, tỷ lệ nối thành công; chưa đo thì ghi chưa đánh giá |
| Khả năng sử dụng | Câu hỏi có thể trả lời; chỉ tiêu có thể tính; mức chi tiết, giới hạn và quyền truy cập cần có |
| Khoảng trống | Điều chưa thể kết luận; dữ liệu/quy tắc cần bổ sung; người cần xác nhận |
| Bằng chứng | Phiên bản/đợt dữ liệu, thời điểm khảo sát, truy vấn kiểm tra và xác nhận của đầu mối |

## 10. Mẫu đề xuất một cách khai thác

Mỗi đề xuất cần nối được dữ liệu với một việc cụ thể của người sử dụng:

1. **Người sử dụng và vấn đề:** Ai đang cần giải quyết việc gì?
2. **Câu hỏi:** Họ muốn biết điều gì, theo phạm vi và thời điểm nào?
3. **Dữ liệu hỗ trợ:** Những bảng/trường nào cung cấp bằng chứng, nối với nhau bằng gì?
4. **Cách xử lý và tính toán:** Quy tắc nghiệp vụ, đơn vị đếm, khử trùng, mốc thời gian và xử lý thiếu.
5. **Đầu ra và hành động:** Chỉ tiêu nào trình bày bằng biểu đồ nào, dashboard nào; bộ lọc, tương tác, báo cáo hoặc danh sách tác nghiệp ra sao; người dùng sẽ làm gì sau khi xem?
6. **Điều kiện khả thi:** Chất lượng, độ bao phủ, cập nhật, phân quyền và phần cần bổ sung.
7. **Mức sẵn sàng:** Đủ điều kiện theo bằng chứng khảo sát / cần làm sạch hoặc liên kết thêm / cần bổ sung dữ liệu / chưa đánh giá.
8. **Nghiệm thu và ưu tiên:** Người xác nhận kết quả, cách đối chiếu, lợi ích kỳ vọng, công sức và phụ thuộc.

Ví dụ giả định: nếu dữ liệu người khuyết tật có mã cá nhân, địa bàn và thời gian hiệu lực phù hợp, có thể đề xuất thống kê số người được ghi nhận theo địa bàn tại ngày chốt. Nếu liên kết thêm được thành viên hộ và tình trạng hộ nghèo đúng thời điểm, có thể đề xuất phân tích phần giao nhau. Muốn biết hỗ trợ đã thực hiện cần thêm dữ liệu thực hiện/chi trả; chỉ có danh sách đối tượng chưa đủ. Tất cả các khả năng trong ví dụ đều phải kiểm chứng trên dữ liệu thực tế.

## 11. Bối cảnh bổ sung về đề nghị hợp tác trọn module

Thông tin bổ sung ngày 22/10/2026: VNPT-IT đề nghị đối tác hợp tác thực hiện module tích hợp dữ liệu từ các CSDL thành phần, tổng hợp và phân tích dữ liệu, từ BA đến phát triển và test. Đây là đề nghị hợp tác, chưa xác nhận hợp đồng/phạm vi đã được nhận. Công nghệ hiện tại được nêu là Angular, Java Spring Boot và Oracle. Giữ tên công ty XVK theo thông tin trước đó; định danh tài khoản trong tin nhắn không được dùng để tự sửa tên pháp nhân.

- Hai nhóm nghiệp vụ đã thống nhất trong trao đổi vẫn là phân tích–tổng hợp và khai thác. Tích hợp là phần công việc nền tảng cần phân tích và phân kỳ cùng hai nhóm này.
- Có kho dữ liệu hiện hữu chưa xác nhận toàn bộ kết nối, lịch nạp, mapping và đối soát đã hoàn chỉnh. Cần phân biệt phần có sẵn, phần sửa và phần xây mới.
- Tuần 26–30/10 lập bản vẽ tổng thể, danh mục use case và lộ trình; đặc tả sâu phần bàn giao đầu tiên vào 15/11.
- Tích hợp gồm TH01 tiếp nhận nguồn, TH02 chuẩn hóa/ánh xạ, TH03 nạp/cập nhật, TH04 đối soát/xử lý lỗi. Danh mục hiện hành gồm 10 PT và 4 KT theo ranh giới được làm rõ ở mục 12.
- Nhân sự BA tuần khảo sát và nhân sự FE/BE/tích hợp/QA triển khai là hai phép tính riêng. Nếu phải xây luồng tích hợp, tính thêm công đặc tả và kiểm thử nguồn–đích; không suy ra tổng nhân sự từ số màn hình.
- Cần xác nhận sớm số nguồn, cách trao đổi, khóa, thêm/sửa/hủy, độ trễ, khối lượng, chạy lại, hạ tầng, môi trường và trách nhiệm vận hành.


## 12. Làm rõ phạm vi phân tích–tổng hợp và đề xuất phương án

Người dùng xác nhận: **phần 1 bao gồm phân tích dữ liệu, tổng hợp dữ liệu, trình bày bằng biểu đồ, dashboard và các đầu ra phân tích**. Do đó dashboard, phân tích tùy chọn và xuất báo cáo phân tích cùng thuộc phần 1. Không chia phần 1 thành tính toán và chuyển toàn bộ giao diện/báo cáo sang phần 2.

BA cần chủ động đề xuất phương án, sau đó khảo sát để kiểm chứng và điều chỉnh. Mỗi phương án phải có câu hỏi nghiệp vụ, dữ liệu, đơn vị và cách tổng hợp, biểu đồ/dashboard, bộ lọc/tương tác, giá trị sử dụng và điều kiện khả thi; không chỉ lập danh sách câu hỏi khảo sát.

| Use case phần 1 | Cách trình bày đề xuất | Dashboard |
|---|---|---|
| PT01 Hiện trạng | Thẻ số người/hộ riêng; thanh nhóm/địa bàn; bảng | DB01 Tổng quan |
| PT02 Cơ cấu | Phân bố tuổi; thanh thuộc tính; cột chồng 100% khi phân lớp loại trừ nhau | DB02 Chuyên đề; tóm tắt DB01 |
| PT03 Giao thoa | Biểu đồ nhiệt theo cặp; bảng chéo; bộ lọc tập giao nhiều điều kiện | DB02 Chuyên đề |
| PT04 So sánh địa bàn | Thanh xếp theo giá trị; biểu đồ nhiệt; bản đồ có điều kiện dữ liệu | DB01/DB02 |
| PT05 Biến động | Đường theo thời gian; cột nhóm cho hai kỳ | DB03 Biến động |
| PT06 Thực hiện hỗ trợ | Cột nhóm phê duyệt/thực hiện; bảng đối soát; đường theo kỳ nếu có lịch sử | DB04 Hỗ trợ và nguồn lực |
| PT07 Độ bao phủ | Ba trạng thái đối chiếu không chồng lấn; cột chồng 100% và bảng lý do | DB04 |
| PT08 Kịch bản nguồn lực | Tham số, bảng kết quả và cột nhóm so phương án | DB04 |
| PT09 Chất lượng/độ phủ dữ liệu | Biểu đồ nhiệt nguồn × quy tắc; thanh độ trễ; bảng lỗi | DB05 Chất lượng dữ liệu |
| PT10 Phân tích tùy chọn/báo cáo | Bảng chéo, biểu đồ phù hợp, lưu cấu hình, xuất báo cáo | Dùng chung DB01–DB05 |

**Phần 2 đề xuất** gồm KT01 tra cứu hồ sơ, KT02 lập danh sách tác nghiệp, KT03 theo dõi xác minh, KT04 cung cấp tập dữ liệu có kiểm soát. Cách tổ chức phần 2 còn cần khách hàng duyệt. Các mã KT đã được sắp xếp lại; dùng danh mục hiện hành trong báo cáo project019_003, không dùng nghĩa cũ của KT01–KT06.

Đề xuất demo đầu tiên: một luồng dữ liệu có đối soát, PT01 + phần PT02/PT04 + mẫu xuất PT10, trình bày trên DB01. Tuần BA vẫn lập bản vẽ toàn bộ 5 dashboard và danh mục use case; đặc tả sâu phần đợt đầu. PT05 cần lịch sử; PT06–PT08 cần dữ liệu chương trình/thực hiện. Chưa có số liệu thật để khẳng định khả thi từng hướng.

Các dải 9–12 và bố trí tròn 11–15 ngày công BA là kịch bản sơ bộ cho lập bản vẽ toàn phạm vi, kiểm chứng mẫu và đặc tả phần đầu; chưa gồm đặc tả đầy đủ cả 5 dashboard, xử lý dữ liệu toàn kho, phát triển/test hoặc hỗ trợ BA sau tuần khảo sát.
