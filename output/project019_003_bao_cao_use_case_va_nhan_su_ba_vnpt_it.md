# Đề xuất phạm vi và nguồn lực triển khai module dữ liệu an sinh xã hội

XVK trình ban giám đốc • Phối hợp VNPT-IT • Ngày 22/10/2026

## 1 Đề xuất để ban giám đốc quyết định

**Đề xuất giải pháp gồm 10 use case phân tích – tổng hợp trên 5 dashboard, cùng các use case khai thác phục vụ công việc.** Phần 1 bao gồm tính toán, phân tích, biểu đồ, dashboard và báo cáo. Tuần 26–30/10 lập bản vẽ tổng thể, sau đó chọn và đặc tả phần triển khai đầu tiên để demo ngày 15/11/2026.

VNPT-IT đã có kho dữ liệu các nhóm đối tượng an sinh của các tỉnh/đơn vị và đề nghị hợp tác làm module từ **BA, phát triển đến test**, có tích hợp từ CSDL thành phần. Công nghệ được nêu: **Angular, Java Spring Boot, Oracle**. Mức hoàn thiện tích hợp và ranh giới công việc mỗi bên cần xác nhận; đây là đề nghị hợp tác, chưa phải phạm vi đã ký.

| Phương án | Nội dung đề xuất | Giá trị và điều kiện |
| --- | --- | --- |
| Nền tảng quản lý hiện trạng | DB01 Tổng quan; DB02 Chuyên đề; DB05 Chất lượng dữ liệu. | Hiểu kho có gì, đối tượng phân bố thế nào, số liệu tin cậy đến đâu. Kiểm chứng khóa, danh mục và hiệu lực. |
| Mở rộng phân tích | DB03 Biến động; DB04 Hỗ trợ và nhu cầu nguồn lực. | Theo dõi thay đổi, thực hiện hỗ trợ và tính kịch bản. Cần lịch sử, chương trình và dữ liệu thực hiện tương ứng. |
| Ứng dụng vào công việc | Tra cứu hồ sơ; lập danh sách tác nghiệp; xác minh; cung cấp dữ liệu có kiểm soát. | Chuyển kết quả phân tích thành đầu việc. Đây là phương án cho phần 2, cần xác nhận quy trình và người dùng. |

**Ưu tiên demo đầu tiên:** một luồng dữ liệu đã đối soát → tổng hợp hiện trạng/cơ cấu → dashboard DB01 có lọc và xem chi tiết tổng hợp → xuất một báo cáo nhất quán. Danh mục toàn dự án vẫn bao phủ các phương án còn lại; không đồng nhất tuần BA với việc chỉ thiết kế demo.

**Nhân sự BA:** đề xuất 2 BA từ đầu, gồm BA đầu mối nghiệp vụ và BA mạnh dữ liệu/SQL. Ước lượng sơ bộ 9–12 ngày công khi tích hợp sẵn sàng; khoảng 11–15 ngày công bố trí khi phải đặc tả thêm một luồng tích hợp. Chuẩn bị BA thứ ba hỗ trợ theo kết quả kiểm tra ngày 27/10. Công phát triển và test được tính riêng.

**Một BA có thể dẫn dắt và lập khung sơ bộ**, nhưng chưa đủ cơ sở cam kết vừa tự khảo sát/xử lý mẫu dữ liệu, vừa kiểm chứng và đặc tả phần đầu đủ triển khai trong 5 ngày. Nhận trọn module và cam kết 15/11 cần chốt dữ liệu, phạm vi, đội triển khai và tiêu chí bàn giao. Các phương án dưới đây là đề xuất BA để thẩm định; chưa phải kết luận từ dữ liệu thực tế.

## 2 Phạm vi tổng thể và cách tổ chức giải pháp

### Phần 1 Phân tích và tổng hợp dữ liệu

Bao gồm đọc hiểu dữ liệu, xây dựng chỉ tiêu, tổng hợp đa chiều, phân tích hiện trạng/cơ cấu/giao thoa/biến động, chọn biểu đồ, thiết kế dashboard, phân tích tùy chọn và lập báo cáo. Đầu ra phải trả lời được một câu hỏi nghiệp vụ bằng số liệu có định nghĩa và cách trình bày phù hợp. **Biểu đồ, dashboard và xuất báo cáo phân tích đều thuộc phần 1.**

### Phần 2 Khai thác dữ liệu

Đề xuất tập trung vào sử dụng dữ liệu trong công việc cụ thể: tra cứu hồ sơ người/hộ; lập danh sách phục vụ rà soát hoặc tổ chức hỗ trợ; giao và theo dõi xác minh; cung cấp tập dữ liệu cho đơn vị được phép. Đây là ranh giới đề xuất để thảo luận, chưa phải định nghĩa phần 2 đã được khách hàng duyệt.

### Chuỗi giải pháp sơ bộ

**CSDL thành phần → tiếp nhận/chuẩn hóa/đối soát → tập dữ liệu nghiệp vụ và chỉ tiêu dùng chung → phân tích, dashboard, báo cáo → tác nghiệp và cung cấp dữ liệu.** Khảo sát để xác định phần có sẵn, phần sửa và phần xây thêm. Chưa có cơ sở quyết định thay kho hiện hữu hoặc xây một lakehouse mới.

| Lớp chức năng | Vai trò đề xuất và điều cần xác nhận |
| --- | --- |
| Dữ liệu và tích hợp | Oracle được nêu cho CSDL; cần làm rõ cấu trúc kho, nguồn, khóa, lịch sử, luồng nạp và các bảng/view có thể dùng lại. |
| Xử lý và cung cấp kết quả | Java Spring Boot theo stack khách hàng; thống nhất nơi thực hiện quy tắc tính, dịch vụ truy vấn, quyền truy cập và cách cập nhật kết quả cùng đội kỹ thuật. |
| Trình bày và sử dụng | Angular theo stack khách hàng; dashboard, bộ lọc, bảng chi tiết, báo cáo và luồng tác nghiệp theo thiết kế BA. Thư viện biểu đồ và thiết kế kỹ thuật chốt sau khảo sát. |

### Nguyên tắc chung cho mọi use case

Đếm riêng người duy nhất, hộ, hồ sơ, lượt hỗ trợ và kinh phí. Một người có thể thuộc nhiều nhóm: không cộng số người của các nhóm thành tổng duy nhất. Tuổi, thành viên hộ, nhóm chính sách và địa bàn phải xét theo ngày chốt. Hiển thị nguồn, kỳ, đơn vị, bộ lọc và tình trạng dữ liệu; thiếu dữ liệu khác với số 0.

Nhóm được nhắc đến: người khuyết tật, thương binh, hộ nghèo, hoàn cảnh khó khăn và diện chính sách; định nghĩa từng nhóm cần xác nhận. Trẻ em chưa được xác nhận thuộc phạm vi. Ý nghĩa của “dân sự” còn mở. Các trường và quan hệ nêu trong đề xuất đều cần kiểm chứng trong kho.

## 3 Use case tích hợp dữ liệu từ CSDL thành phần

Tích hợp là phần công việc đã được nêu trong đề nghị hợp tác. Nhóm use case hỗ trợ dưới đây cung cấp dữ liệu cho hai nhóm nghiệp vụ phân tích – tổng hợp và khai thác. Các mục là đề xuất để khảo sát; cần phân biệt luồng đã có, luồng cần sửa và luồng phải xây mới.

| Mã và use case | Tác nhân và nhu cầu | Luồng và kết quả | Điểm BA phải làm rõ |
| --- | --- | --- | --- |
| TH01<br>Tiếp nhận dữ liệu nguồn | Cán bộ vận hành/đầu mối nguồn cung cấp dữ liệu cho module. | Chọn nguồn, phạm vi và kỳ → nhận dữ liệu qua phương thức đã duyệt → ghi nguồn, phiên nhận và trạng thái. | CSDL/API/tệp; quyền đọc; cấu trúc, khối lượng, lịch và cơ chế báo lỗi. |
| TH02<br>Chuẩn hóa và ánh xạ | Quản trị dữ liệu đưa các nguồn về nghĩa và cấu trúc thống nhất. | Áp dụng mapping trường, mã và đơn vị → xác định khóa → tách bản ghi chưa hợp lệ → tạo dữ liệu chuẩn hóa có dấu vết. | Khóa cá nhân/hộ; mã địa bàn; quy tắc ưu tiên nguồn; hiệu lực và trường hợp không nối được. |
| TH03<br>Nạp và cập nhật dữ liệu | Cán bộ vận hành hoặc lịch hệ thống duy trì tập dữ liệu đích. | Nạp ban đầu hoặc phần thay đổi → xử lý thêm/sửa/hủy theo quy tắc → cập nhật mốc xử lý và lịch sử cần giữ. | Nạp toàn bộ/gia tăng; nhận biết thay đổi; dữ liệu đến muộn; chạy lại không sinh bản ghi trùng. |
| TH04<br>Đối soát và xử lý lỗi | Vận hành/kiểm soát dữ liệu xác nhận mỗi đợt tích hợp. | Đối chiếu nguồn–đích → xem lỗi và chênh lệch → xử lý nguyên nhân → chạy lại phần phù hợp → lưu kết quả kiểm tra. | Nhóm trạng thái không chồng lấn; điều kiện hoàn tất; người xử lý; cách phục hồi và truy vết. |

### Đầu ra khảo sát tích hợp trong tuần đầu

Lập sơ đồ các CSDL thành phần và luồng vào kho; danh mục giao tiếp nguồn–đích; tình trạng hiện hữu; chủ nguồn; định nghĩa dữ liệu trao đổi, chu kỳ và mức độ trễ chấp nhận. Bao phủ các nguồn trong phạm vi dự án; kiểm tra sâu một luồng đại diện để đặc tả đợt đầu và tìm rủi ro có thể ảnh hưởng các nguồn khác.

### Tiêu chí kiểm chứng cho luồng được chọn

Đối soát số bản ghi nhận, hợp lệ và lỗi theo nhóm không chồng lấn; chứng minh dữ liệu đích đúng mapping. Có trường hợp thêm mới, sửa, bản ghi không hợp lệ và chạy lại cùng đợt. Hủy/xóa và dữ liệu đến muộn được kiểm tra theo quy tắc đã thống nhất. Giữ dấu vết nguồn, đợt nạp, thời điểm và lỗi; không tự xóa hoặc sửa dữ liệu gốc.

Đội kỹ thuật xác nhận cách kết nối và xử lý phù hợp nền tảng; BA đặc tả hành vi và kết quả cần đạt. Thông tin “đã có kho” và yêu cầu “tích hợp CSDL thành phần” có thể cùng đúng: nhiệm vụ khảo sát là xác định khoảng cách giữa luồng đang chạy và module được đặt hàng.

## 4 Phần 1 Phân tích hiện trạng và đặc điểm đối tượng

PT01–PT05 phục vụ lãnh đạo, cán bộ phân tích và cán bộ nghiệp vụ. Người dùng chọn kỳ, địa bàn và nhóm; hệ thống tính trên tập dữ liệu đã thống nhất, trình bày kết quả và cho xem sâu theo quyền. Mỗi hàng dưới đây là một use case đề xuất, không phải chỉ một màn hình.

| Use case và câu hỏi | Chỉ tiêu / cách tổng hợp | Biểu đồ và tương tác | Dữ liệu cần / giá trị |
| --- | --- | --- | --- |
| PT01<br>Tổng hợp hiện trạng<br>Có bao nhiêu người/hộ thuộc từng nhóm ở thời điểm chốt? | Đếm người duy nhất theo khóa trong phạm vi; đếm hộ riêng. Tổng hợp theo nhóm và địa bàn; nếu khóa chưa tin cậy, chỉ công bố số hồ sơ đúng nhãn. | DB01: thẻ số tổng; thanh ngang theo nhóm/địa bàn; bảng tổng hợp. Chọn thanh để lọc các ô còn lại và mở chi tiết tổng hợp. | Khóa, nhóm, địa bàn, thời gian hiệu lực. Giúp nắm quy mô quản lý, chuẩn bị báo cáo và xác định nơi cần xem sâu. |
| PT02<br>Phân tích cơ cấu<br>Đối tượng có những đặc điểm gì? | Phân tổ tuổi tại ngày chốt, thuộc tính và loại/mức độ theo dữ liệu có sẵn; số lượng và tỷ trọng trong tập đã chọn; giữ nhóm chưa rõ. | DB02: cột phân bố tuổi; thanh theo thuộc tính. Cột chồng 100% chỉ khi các lớp loại trừ nhau. Chọn tổ để lọc bảng chi tiết. | Ngày sinh/tuổi và thuộc tính có nghĩa rõ ràng. Giúp hiểu nhu cầu theo đặc điểm; không tự suy ra nhu cầu dịch vụ chỉ từ một nhãn nhóm. |
| PT03<br>Phân tích giao thoa<br>Bao nhiêu người đồng thời thuộc các nhóm cần quan tâm? | Đếm giao của hai hoặc nhiều điều kiện. Ví dụ người khuyết tật là thành viên hộ nghèo tại ngày chốt; không cộng các ô giao thành tổng. | DB02: biểu đồ nhiệt giao thoa theo cặp và bảng chéo; bộ lọc nhiều điều kiện cho tập giao cụ thể. Chọn ô để xem số liệu theo địa bàn. | Khóa cá nhân–hộ, quan hệ thành viên và hiệu lực phân loại. Giúp nhận diện tập cần xem xét phối hợp hỗ trợ. |
| PT04<br>So sánh địa bàn<br>Địa bàn khác nhau thế nào về quy mô và cơ cấu? | So sánh số lượng; tính tỷ lệ khi có mẫu số phù hợp và cùng kỳ. Ghi độ phủ nguồn, phạm vi và danh mục địa bàn. | DB01/DB02: thanh xếp theo giá trị; biểu đồ nhiệt địa bàn × nhóm. Bản đồ là phương án bổ sung khi có ranh giới/mã phù hợp. | Cùng định nghĩa, kỳ và phạm vi so sánh. Giúp chọn địa bàn khảo sát sâu; số lớn đơn thuần chưa chứng minh nhu cầu cao hơn. |
| PT05<br>Phân tích biến động<br>Quy mô/cơ cấu thay đổi ra sao qua các kỳ? | Chênh lệch số lượng và phần trăm khi kỳ gốc khác 0; tách vào/ra nhóm nếu có lịch sử đủ. Gắn ghi chú khi thay đổi nguồn/phạm vi. | DB03: đường theo chuỗi thời gian; hai kỳ dùng cột nhóm. Chọn đoạn/kỳ để phân rã theo địa bàn, nhóm và xem bảng thay đổi. | Ít nhất hai kỳ so sánh được; lịch sử cần thiết. Giúp theo dõi thay đổi, đặt câu hỏi nguyên nhân; không suy ra tác động chính sách từ tương quan. |

Quy tắc tỷ trọng: mẫu số phải hiển thị hoặc xem được. Những nhóm có thể chồng lấn không dùng biểu đồ tròn hoặc cột chồng 100% để thể hiện cơ cấu. Phần chưa rõ thông tin phải được nhìn thấy; kỳ thiếu dữ liệu không tự nối thành xu hướng liên tục.

## 5 Phần 1 Phân tích hỗ trợ và chất lượng dữ liệu

| Use case và câu hỏi | Chỉ tiêu / cách tổng hợp | Biểu đồ và tương tác | Dữ liệu cần / giá trị |
| --- | --- | --- | --- |
| PT06<br>Tổng hợp thực hiện hỗ trợ<br>Đã phê duyệt và thực hiện đến đâu? | Tách số người, lượt hỗ trợ và kinh phí; tổng hợp theo chương trình, địa bàn, kỳ và trạng thái. Xử lý hủy/điều chỉnh theo quy tắc. | DB04 – Thực hiện: cột nhóm phê duyệt/thực hiện; đường kinh phí theo kỳ nếu có lịch sử; bảng đối soát. Chọn chương trình để xem sâu. | Chương trình, quyết định, thực hiện/chi trả và khóa nối. Giúp theo dõi tiến độ; không dùng lượt chi trả thay số người được hỗ trợ. |
| PT07<br>Phân tích độ bao phủ<br>Trường hợp nào cần xác minh việc tiếp cận hỗ trợ? | Trong danh sách đủ điều kiện đã xác nhận, phân trạng thái không chồng lấn: đã có ghi nhận; chưa tìm thấy; chưa đủ dữ liệu đối chiếu. Công khai phần chưa xác định. | DB04 – Đối soát: cột chồng 100% theo ba trạng thái; bảng số lượng/lý do. Chọn phần cần rà soát để xem nhóm hoặc chuyển sang lập danh sách KT02. | Danh sách đủ điều kiện, kỳ và dữ liệu thực hiện đủ phạm vi. Giúp khoanh vùng xác minh; thiếu bản ghi không có nghĩa là chưa được hưởng. |
| PT08<br>Phân tích nguồn lực theo kịch bản<br>Cần bao nhiêu nguồn lực với các giả định hỗ trợ? | Người dùng chọn tập đối tượng, mức hỗ trợ và số kỳ; tính theo quy tắc chương trình, trùng hưởng và giới hạn đã duyệt. So sánh các phương án. | DB04 – Kịch bản: bảng tham số/kết quả; cột nhóm so kinh phí hoặc lượt. Thay tham số để tính lại; luôn gắn nhãn giả định. | Định mức, tập đối tượng và quy tắc hợp lệ. Hỗ trợ cân nhắc kế hoạch; kết quả là kịch bản, chưa phải dự báo hoặc khoản chi được phê duyệt. |
| PT09<br>Phân tích chất lượng/độ phủ<br>Nguồn nào dùng được và còn vướng ở đâu? | Theo nguồn: tỷ lệ thiếu trường bắt buộc, vi phạm khóa/mã, độ trễ cập nhật, tỷ lệ nối được. Mỗi phép đo có mẫu số và quy tắc riêng. | DB05: biểu đồ nhiệt nguồn × quy tắc; thanh độ trễ; bảng lỗi/độ phủ. Chọn ô để xem bằng chứng và chuyển luồng xử lý TH04. | Metadata, kết quả kiểm tra và lịch nạp. Giúp biết giới hạn số liệu và ưu tiên sửa; các loại lỗi có thể cùng nằm trên một hồ sơ, không cộng tỷ lệ lỗi. |
| PT10<br>Phân tích tùy chọn và báo cáo<br>Có thể xem/tổng hợp theo nhu cầu cụ thể nào? | Chọn chỉ tiêu, chiều và bộ lọc được hỗ trợ; dùng cùng định nghĩa chuẩn; xem bảng chéo, lưu cấu hình và xuất báo cáo có kỳ/nguồn. | Dùng chung DB01–DB05: bảng chéo, thanh so nhóm hoặc đường theo thời gian khi phù hợp. Đợt đầu dùng một mẫu cố định có lọc/xuất. | Danh mục chỉ tiêu–chiều được phép kết hợp và quyền xuất. Giảm tổng hợp thủ công, thống nhất số trên dashboard và báo cáo. |

PT06–PT08 cần dữ liệu chương trình và hỗ trợ thực tế, chưa xác nhận kho đã có. PT07 chỉ tính độ bao phủ khi mẫu số đủ điều kiện và dữ liệu đối chiếu đã được xác nhận; nếu chưa đủ, hiển thị trạng thái chưa thể kết luận. PT08 cần tách giả định khỏi thực tế. PT09 mô tả độ tin cậy dữ liệu, không phải chấm điểm con người.

**PT10 nằm trong phần 1.** Xuất báo cáo phân tích khác với cung cấp một tập dữ liệu cấp hồ sơ để đơn vị khác dùng lại ở KT04. Phân tích tùy chọn không mặc định cho phép người dùng nối mọi bảng hoặc tự tạo mọi công thức.

## 6 Phương án 5 dashboard cho phần 1

Đề xuất bố cục và hành vi để khách hàng lựa chọn trong tuần BA. Đây là thiết kế sản phẩm, chưa phải dashboard có dữ liệu thật. Các màn hình dùng chung định nghĩa chỉ tiêu; không tạo năm bộ công thức độc lập.

| Dashboard / người dùng | Các khối trên màn hình | Bộ lọc và hành động |
| --- | --- | --- |
| DB01 Tổng quan an sinh<br>Lãnh đạo, quản lý<br>PT01; tóm tắt PT02/PT04 | Trên: số người duy nhất, số hộ, phạm vi nguồn/địa bàn và lần cập nhật. Giữa: thanh theo nhóm và theo địa bàn. Dưới: cơ cấu của nhóm được chọn và bảng số liệu. | Kỳ/ngày chốt, nhóm, địa bàn, nguồn. Chọn thanh lọc các khối liên quan; mở DB02; xuất mẫu PT10. Giữ số người và số hộ ở các khối có đơn vị riêng. |
| DB02 Chuyên đề đối tượng<br>Cán bộ phân tích/nghiệp vụ<br>PT02–PT04 | Tổng nhóm được chọn; phân bố tuổi/thuộc tính; biểu đồ nhiệt giao thoa; bảng chéo nhóm–địa bàn. Tái dùng bố cục cho khuyết tật, hộ nghèo, thương binh… theo dữ liệu phù hợp. | Chọn chuyên đề, thời điểm, địa bàn, thuộc tính; chọn ô giao thoa để xem tập tổng hợp. Chuyển tra cứu hồ sơ KT01 chỉ khi có quyền. |
| DB03 Biến động<br>Cán bộ quản lý/phân tích<br>PT05 | Giá trị hiện tại/kỳ trước, chênh lệch; đường theo thời gian; cột so địa bàn/nhóm; bảng vào/ra nếu có lịch sử; ghi chú thay đổi phạm vi dữ liệu. | Khoảng thời gian, kỳ so, nhóm, địa bàn. Chọn điểm/kỳ để phân rã. Khi chỉ có hai kỳ, dùng so sánh hai kỳ; khi thiếu lịch sử, đánh dấu chưa đáp ứng. |
| DB04 Hỗ trợ và nguồn lực<br>Cán bộ chương trình/kế hoạch<br>PT06–PT08 | Ba tab: Thực hiện, Đối soát, Kịch bản. Lần lượt có cột phê duyệt/thực hiện; tỷ trọng ba trạng thái đối chiếu; bảng tham số và cột so phương án nguồn lực. | Chương trình, kỳ, địa bàn, nhóm, trạng thái. Xem lý do chênh lệch; tạo danh sách KT02; thay tham số kịch bản. Phân biệt người, lượt và tiền. |
| DB05 Chất lượng dữ liệu<br>Vận hành, BA, chủ dữ liệu<br>PT09 | Độ phủ nguồn, lần cập nhật và số bản ghi được kiểm tra; biểu đồ nhiệt theo quy tắc; thanh độ trễ; bảng lỗi, thiếu danh mục hoặc chưa nối được. | Nguồn, đợt nạp, nhóm quy tắc, địa bàn. Xem mẫu lỗi có quyền; mở TH04 để xử lý. Theo dõi độ tin cậy trước khi dùng chỉ tiêu quản lý. |

### Ví dụ luồng DB01 cần đặc tả cho đợt đầu

Chọn ngày chốt, địa bàn và nhóm → xác định tập hồ sơ có hiệu lực → đếm theo khóa đã kiểm chứng → hiển thị thẻ, thanh và bảng → chọn một thanh để lọc sâu → xem nguồn/quy tắc → xuất báo cáo PT10. Trường hợp thiếu khóa, thiếu địa bàn, nhiều nhóm hoặc hết hiệu lực đều có cách xử lý được duyệt.

### Tiêu chí chung cho biểu đồ, bộ lọc và báo cáo

Mỗi khối có tên chỉ tiêu, đơn vị, kỳ và phạm vi. Bộ lọc tác động nhất quán tới các khối liên quan; ngoại lệ phải ghi rõ. Số trên thẻ, biểu đồ, bảng và tệp xuất khớp truy vấn đối chiếu cùng tập dữ liệu. Hiển thị “chưa có dữ liệu” riêng với 0; giữ nhóm chưa rõ. Quyền xem/xuất được áp dụng cả khi mở chi tiết. Màu đi kèm nhãn/chú giải; cột so sánh số lượng bắt đầu từ 0.

## 7 Phần 2 Khai thác dữ liệu phục vụ công việc

Bốn use case dưới đây là phương án đề xuất để làm rõ yêu cầu khai thác. Mục đích là chuyển dữ liệu và kết quả phân tích thành công việc cụ thể; cần VNPT-IT và đơn vị sử dụng xác nhận tác nhân, quy trình và mức ưu tiên. Dashboard, phân tích tùy chọn và báo cáo đã nằm ở phần 1.

| Use case | Người dùng và mục đích | Luồng / đầu ra | Điều kiện và kiểm chứng |
| --- | --- | --- | --- |
| KT01<br>Tra cứu hồ sơ người/hộ | Cán bộ nghiệp vụ kiểm tra thông tin một người hoặc hộ. | Tìm theo tiêu chí được phép → xem danh sách → mở hồ sơ, các nhóm, quan hệ hộ, nguồn và lịch sử có sẵn. | Khóa nối đã kiểm chứng, phân quyền theo vai trò/địa bàn. Hồ sơ có nguồn; liên kết chưa chắc chắn được đánh dấu, không tự gộp. |
| KT02<br>Lập danh sách tác nghiệp | Cán bộ phụ trách lập danh sách phục vụ khảo sát, xác minh hoặc tổ chức hoạt động hỗ trợ. | Chọn tập từ PT03/PT07 hoặc điều kiện đã duyệt → kiểm tra phạm vi → lưu danh sách có tiêu chí, ngày chốt, phiên bản và người phụ trách. | Tiêu chí có chủ thể xác nhận; danh sách khớp tập lọc và có thể truy vết. Tạo danh sách không tự xác định đủ điều kiện hoặc quyết định quyền lợi. |
| KT03<br>Theo dõi xác minh | Cán bộ được giao và quản lý theo dõi các trường hợp cần làm rõ. | Nhận danh sách → phân công → ghi kết quả/bằng chứng → rà soát, xác nhận hoàn tất hoặc trả lại. | Cần quy trình, người xử lý, trạng thái và thời hạn được duyệt. Thay đổi có dấu vết; kết quả không tự ghi đè CSDL nguồn khi chưa có cơ chế thống nhất. |
| KT04<br>Cung cấp tập dữ liệu | Đầu mối được ủy quyền đáp ứng nhu cầu dùng lại dữ liệu của đơn vị khác. | Xác định mục đích, bên nhận, trường và phạm vi → kiểm tra quyền/phê duyệt theo quy trình → cung cấp tệp hoặc giao diện đã thống nhất → lưu dấu vết. | Danh mục trường, quyền nhận, phương thức và kỳ cập nhật. Chỉ cung cấp đúng phạm vi; kiểm chứng dữ liệu đầu ra và nhật ký cung cấp. |

### Ví dụ sử dụng xuyên suốt hai phần

Cán bộ chọn chuyên đề người khuyết tật và điều kiện thành viên hộ nghèo. PT03 xác định tập giao theo ngày chốt; DB02 trình bày số lượng theo địa bàn và bảng chéo. Sau khi xem kết quả, cán bộ tạo danh sách rà soát bằng KT02, giao việc qua KT03, mở hồ sơ KT01 khi cần đối chiếu. Báo cáo kết quả tổng hợp vẫn thuộc PT10 của phần 1.

### Cách giới hạn phần khai thác trong đợt đầu

Tuần BA phải đề xuất cả bốn use case, kể cả mục xếp đợt sau. Demo 15/11 ưu tiên luồng phân tích tổng quan; có thể thêm tra cứu KT01 nếu nguồn lực, dữ liệu và quyền đã đáp ứng. Chưa mặc định phải xây quy trình tác nghiệp hoặc API chia sẻ ngay trong đợt đầu. Lựa chọn này cần được ghi rõ trong biên bản duyệt phạm vi.

## 8 Công sức BA theo mức sẵn sàng của tích hợp

BA vẫn phải khảo sát toàn phạm vi hai nhóm nghiệp vụ và phần tích hợp liên quan. Lập phương án cho 10 PT, 5 dashboard và nhóm KT; chỉ đặc tả sâu dashboard tổng quan DB01 và luồng dữ liệu đợt 1. Chưa gồm đặc tả chi tiết toàn bộ 5 dashboard hoặc xử lý dữ liệu toàn kho. Giả định có quyền đọc từ ngày đầu, đầu mối giải nghĩa phản hồi trong ngày, kiểm tra mẫu đại diện và một vòng duyệt chính. Công lập trình, sửa pipeline và test phần mềm được ước lượng riêng.

| Nhóm việc cơ sở | Giờ BA |
| --- | --- |
| Chốt mục tiêu, tác nhân và phạm vi | 6–8 |
| Kiểm kê nguồn và giải nghĩa dữ liệu | 10–14 |
| Kiểm tra chất lượng mẫu và thử liên kết | 10–14 |
| Danh mục use case, phương án dashboard và ma trận bao phủ | 10–12 |
| Mô hình, định nghĩa chung và phân kỳ | 6–8 |
| Đặc tả đợt 1, phác thảo và tiêu chí nghiệm thu | 12–16 |
| Review, phối hợp, chỉnh sửa và bàn giao | 6–8 |
| Tổng cơ sở khi tích hợp đã sẵn sàng | 60–80 |

### Phần tăng thêm khi phải xây luồng tích hợp

Dự trù thêm **8–16 giờ cơ sở** cho một luồng đại diện được chọn ở đợt 1: làm rõ giao tiếp và trách nhiệm nguồn 3–6 giờ; hành vi cập nhật/chạy lại 3–6 giờ; đối soát và tiêu chí lỗi 2–4 giờ. Mapping trường và profiling đã có trong phần cơ sở, không cộng lại. Nhiều kiểu nguồn hoặc luồng phức tạp cần ước lượng riêng.

| Kịch bản | Tổng giờ có dự phòng 20 phần trăm | Ngày công 8 giờ |
| --- | --- | --- |
| A  Tích hợp đã có và dùng được | 72–96 | 9–12 |
| B  Phải đặc tả thêm luồng tích hợp | 81,6–115,2 | 10,2–14,4; bố trí 11 đến 15 |

Đây là hai kịch bản lập kế hoạch trước khảo sát, không phải định mức năng suất. Kịch bản B chưa bao gồm viết bộ kết nối, xử lý dữ liệu toàn kho hoặc xây dựng lịch nạp vận hành. Cuối 27/10 phải xác định kịch bản thực tế, số nguồn/luồng khó và khả năng tái sử dụng để tính lại công sức.

### Hệ quả đối với số lượng BA

**1 BA trong 5 ngày có 40 giờ:** chưa đủ so với cả hai dải; có thể dẫn dắt và lập khung nhưng mức kiểm chứng/đặc tả phải được thỏa thuận. **2 BA có 80 giờ:** phù hợp để khởi động; kịch bản A có thể cần thêm 1–2 ngày hỗ trợ. Kịch bản B cần thêm khoảng 1–5 ngày công BA có năng lực tích hợp; 3 BA đủ 5 ngày tạo 120 giờ năng lực danh nghĩa.

Bố trí thêm người chỉ có ích khi tách được đầu việc và có dữ liệu để làm. Đề xuất 1 BA đầu mối và 1 BA dữ liệu ngay từ đầu, chuẩn bị BA thứ ba theo kết quả khảo sát. Thời gian chờ truy cập, chủ nguồn hoặc người duyệt cần xử lý bằng điều phối. Một tuần vẫn phải bao quát bản vẽ tổng thể, dù số người hoặc độ sâu đặc tả thay đổi.

## 9 Bản vẽ nghiệp vụ bàn giao sau tuần đầu

**Ngày 30/10 cần biết toàn dự án sẽ làm gì, trình bày dữ liệu như thế nào và triển khai từng phần ra sao.** Đề xuất bao quát toàn phạm vi; kiểm chứng sâu và đặc tả đủ xây dựng cho phần đợt 1. Không cần đặc tả chi tiết mọi use case trong một tuần.

| Sản phẩm | Bao quát toàn module | Chi tiết đủ triển khai cho đợt 1 |
| --- | --- | --- |
| Phạm vi và danh mục use case | Hai nhóm yêu cầu; TH01–TH04, PT01–PT10, KT01–KT04; tác nhân, giá trị, điều kiện và ưu tiên. | Luồng chính/ngoại lệ của phần được chọn; tiêu chí chấp nhận và ranh giới bàn giao. |
| Bản đồ dữ liệu và tích hợp | Nguồn, ý nghĩa, độ phủ, chủ nguồn; luồng đã có/cần sửa/xây mới; mô hình người–hộ–nhóm–địa bàn–thời gian. | Mapping nguồn–đích; khóa, hiệu lực, cập nhật, lỗi và đối soát một luồng đại diện. |
| Danh mục chỉ tiêu | Câu hỏi, thước đo, đơn vị, chiều phân tích và điều kiện dữ liệu cho mỗi PT. | Công thức, mẫu số, quy tắc khử trùng/nối nguồn, dữ liệu thiếu và truy vấn kiểm chứng. |
| Phương án biểu đồ/dashboard | Bố cục và vai trò 5 dashboard; chỉ tiêu trên từng khối, bộ lọc và cách chuyển giữa màn hình. | Phác thảo DB01 và mẫu xuất; trạng thái đủ/thiếu dữ liệu, tương tác, quyền và dữ liệu kỳ vọng. |
| Lộ trình và truy vết | Use case nào đợt đầu, đợt sau hoặc chờ dữ liệu; lý do, phụ thuộc và điểm mở. | Phạm vi 15/11, kế hoạch phát triển/test, người phụ trách và mốc xử lý phụ thuộc. |
| Bộ bàn giao và xác nhận | Nội dung đã duyệt, chưa duyệt; người xác nhận và hạn giải quyết. | Bộ mẫu cùng kết quả đúng; không còn điểm mở chặn việc thực hiện phần đã cam kết. |

**Chuỗi truy vết:** câu hỏi nghiệp vụ → use case → nguồn/trường → quy tắc tổng hợp → chỉ tiêu → biểu đồ/dashboard hoặc đầu ra tác nghiệp → tiêu chí kiểm chứng → đợt triển khai. Ví dụ PT01 → hồ sơ có hiệu lực → đếm khóa duy nhất → thẻ/thanh/bảng DB01 → khớp truy vấn và tệp xuất → đợt đầu.

### Phối hợp BA, phát triển và test

BA đầu mối phụ trách nghiệp vụ, phương án dashboard và phối hợp trình duyệt phạm vi; BA dữ liệu tự khảo sát, truy vấn mẫu, mapping và kiểm chứng chỉ tiêu. Kỹ thuật phụ trách thiết kế, Angular, Java Spring Boot, Oracle/tích hợp; QA kiểm tra số liệu nguồn–đích–API–giao diện–tệp xuất, quy tắc và quyền. Một người có thể kiêm vai trò phù hợp nhưng công sức từng phần phải được tính đủ.

Chưa đủ dữ liệu để chốt số lập trình viên/tester. Cần ước lượng riêng kết nối, xử lý dữ liệu, API, biểu đồ/báo cáo, tác nghiệp, triển khai và kiểm thử theo phần được chọn; không lấy 2 BA làm tổng nhân sự thực hiện module.

## 10 Kế hoạch một tuần khảo sát và lập bản vẽ

Lịch đề xuất **26–30/10/2026**, nếu hợp tác được thông qua. BA tự khảo sát/xử lý mẫu; VNPT-IT cần cấp quyền và bố trí đầu mối xác nhận ý nghĩa nghiệp vụ. Đầu mối xác nhận không được mặc định là kỹ sư dữ liệu làm thay phần việc BA.

| Ngày | BA đầu mối nghiệp vụ | BA dữ liệu / phối hợp | Kết quả và điểm chốt |
| --- | --- | --- | --- |
| Thứ 2<br>26/10 | Xác nhận mục tiêu hai phần, vai trò; trình 10 PT/5 dashboard/4 KT để khách hàng phản biện và chọn hướng. | Kiểm kê nguồn, trường và quan hệ; xác định luồng hiện hữu; chọn mẫu đại diện và quyền truy cập. | Bản đồ sơ bộ toàn phạm vi; danh mục dữ liệu/câu hỏi; không chờ hết khảo sát mới đưa ý tưởng. |
| Thứ 3<br>27/10 | Định nghĩa chỉ tiêu, mục đích biểu đồ và nhu cầu từng dashboard; xác định các quy trình khai thác. | Kiểm tra khóa, chất lượng, hiệu lực, lịch sử; thử liên kết; kiểm tra dữ liệu hỗ trợ có hay không. | Đánh dấu từng phương án đủ điều kiện/cần sửa/cần bổ sung/chưa đánh giá; chốt bổ sung BA và rủi ro. |
| Thứ 4<br>28/10 | Hoàn thiện danh mục tổng thể, bố cục 5 dashboard và phân kỳ; chọn luồng DB01 cho đợt đầu. | Mapping và tính thử chỉ tiêu của đợt đầu; viết quy tắc/ngoại lệ tích hợp và đối soát. | Review giữa tuần: thống nhất toàn bộ sẽ làm gì, phần nào triển khai trước, phần nào phụ thuộc dữ liệu. |
| Thứ 5<br>29/10 | Đặc tả DB01, bộ lọc, bảng, mẫu xuất, quyền và luồng; rà soát cùng phát triển/QA. | Chuẩn bị mẫu và kết quả kỳ vọng; kiểm chứng công thức/đếm trùng; xử lý điểm mở chặn đợt đầu. | Bộ đặc tả phần đầu đủ để đội kỹ thuật ước lượng; giữ danh mục các phần sau trong bản vẽ. |
| Thứ 6<br>30/10 | Trình duyệt phạm vi tổng thể, use case, phương án biểu đồ/dashboard và kế hoạch 15/11. | Bàn giao mapping, dữ liệu kiểm chứng, giới hạn đã biết; thống nhất hỗ trợ BA trong giai đoạn xây dựng. | Biên bản xác nhận, backlog phân kỳ, bộ đặc tả đợt 1, người phụ trách và hạn xử lý điểm mở. |

### Điều kiện để kế hoạch một tuần thực hiện được

Có quyền đọc và tài liệu nguồn ngay ngày đầu; đầu mối giải nghĩa phản hồi trong ngày; chủ thể có thẩm quyền duyệt trong tuần. Hai BA chia việc nhưng dùng chung định nghĩa và checkpoint hằng ngày. Nếu chưa tiếp cận dữ liệu, vẫn có thể hoàn thiện phương án nghiệp vụ nhưng phải ghi rõ phần chưa kiểm chứng, không đánh dấu sẵn sàng triển khai.

BA thứ ba, nếu cần, nhận phần tách được như nguồn/luồng tích hợp bổ sung hoặc chuẩn hóa từ điển, giải phóng hai BA chính cho định nghĩa nghiệp vụ và đặc tả phần đầu. Năng lực thêm người không thay thế quyền truy cập hoặc quyết định của khách hàng.

## 11 Phần demo đầu tiên và lộ trình triển khai

### Đề xuất mục tiêu ngày 15/11

Chứng minh luồng **dữ liệu nguồn → chuẩn hóa/đối soát → chỉ tiêu hiện trạng/cơ cấu → DB01 → báo cáo PT10** chạy được trên phạm vi mẫu được duyệt. Phạm vi đề nghị: một luồng nguồn đại diện, một hoặc hai nhóm đối tượng và số địa bàn do khảo sát xác nhận; không mặc định tích hợp toàn bộ nguồn ngay đợt đầu.

| Đợt | Use case / sản phẩm | Điều kiện và cách đánh giá |
| --- | --- | --- |
| Đợt 1<br>Demo 15/11 | TH01–TH04 ở luồng được chọn; PT01, phần cơ cấu đơn giản PT02, một chiều địa bàn PT04 và mẫu xuất PT10; dashboard DB01. | Dữ liệu thật được phép dùng hoặc bộ dữ liệu kiểm thử đã duyệt và gắn nhãn. Đối chiếu đầu–cuối; xác nhận bộ lọc, quyền và xử lý ngoại lệ. |
| Mở rộng hiện trạng | Đầy đủ PT02–PT04; DB02; PT09/DB05; KT01 và PT10 nâng cao theo ưu tiên. | Có liên kết cá nhân–hộ/nhóm và quy tắc chất lượng. Quy tắc kiểm tra dữ liệu vẫn cần ở đợt 1; giao diện DB05 có thể làm sau. |
| Mở rộng lịch sử/hỗ trợ | PT05–PT08; DB03–DB04; KT02–KT04 theo nhu cầu và quy trình đã duyệt. | Có lịch sử so sánh được, dữ liệu chương trình/thực hiện và đầu mối xử lý. Có thể đổi thứ tự theo dữ liệu và giá trị thực tế. |

### Tiêu chí demo đợt đầu

Có ví dụ bình thường và ngoại lệ: khóa trùng, thuộc nhiều nhóm, thiếu địa bàn/thuộc tính, hết hiệu lực, chạy lại đợt nạp. Số thẻ, biểu đồ, bảng và tệp xuất khớp kết quả đã kiểm chứng; ngày chốt, nguồn và đơn vị rõ ràng. Lọc địa bàn/nhóm tác động đúng; người không đủ quyền không xem/xuất ngoài phạm vi. Đo thời gian phản hồi trên tập và môi trường đã thống nhất, với ngưỡng do hai bên chốt.

Nếu chỉ dùng dữ liệu mô phỏng, demo chứng minh chức năng và quy tắc trên bộ mẫu; chưa chứng minh kết nối, chất lượng hay hiệu năng của dữ liệu thật. Tình trạng này phải thể hiện trong biên bản bàn giao.

### Nhịp triển khai sau khi duyệt bản vẽ

**02–06/11:** đội triển khai thực hiện luồng dữ liệu, dịch vụ chỉ tiêu và giao diện; BA giải đáp/kiểm chứng theo từng phần. **09–12/11:** tích hợp đầu–cuối, test số liệu, quyền và lỗi; sửa các điểm chặn demo. **13/11:** chạy thử và chuẩn bị nội bộ. **15/11 là Chủ nhật:** xác nhận lịch demo với các bên. Kế hoạch cần đội kỹ thuật ước lượng và xác nhận ngay khi duyệt 30/10.

BA tiếp tục tham gia giải đáp và nghiệm thu trong giai đoạn phát triển; công này chưa nằm trong 9–12 hoặc 11–15 ngày công khảo sát ở mục 8. Kế hoạch tiến độ là đề xuất để thẩm định, chưa phải cam kết triển khai khi chưa có đội và dữ liệu.

## 12 Điều kiện nhận việc và quyết định cần chốt

### Những gì đã biết và những gì phải kiểm chứng

Đã biết từ trao đổi: có kho dữ liệu; hai nhóm yêu cầu phân tích–tổng hợp và khai thác; phần 1 bao gồm biểu đồ/dashboard; có tích hợp CSDL thành phần; stack Angular, Java Spring Boot, Oracle; đề nghị hợp tác BA–phát triển–test; BA tự khảo sát/xử lý dữ liệu; một tuần lập bản vẽ và mốc demo 15/11. Chưa có dữ liệu mẫu hoặc cấu trúc trong cuộc trò chuyện.

| Yếu tố | Ảnh hưởng | Cách xử lý đề xuất |
| --- | --- | --- |
| Số nguồn, bảng và mức sẵn sàng chưa rõ | Có thể vượt dải công BA, tích hợp hoặc test dự kiến. | Kiểm kê toàn phạm vi; kiểm chứng mẫu đại diện; cập nhật ước lượng ngày 27/10, ghi rõ phần chưa kiểm tra. |
| Khóa, danh mục, hiệu lực hoặc quan hệ hộ không tin cậy | Sai số người duy nhất, cơ cấu, giao thoa hoặc so sánh địa bàn. | Chốt định nghĩa và quy tắc; chỉ công bố chỉ tiêu có bằng chứng; giữ phần thiếu/chưa nối được. |
| Không có lịch sử hoặc dữ liệu chương trình hỗ trợ | Chưa làm được DB03 hoặc các tab DB04 tương ứng. | Giữ use case trong bản vẽ; ghi rõ dữ liệu cần bổ sung, người phụ trách và điều kiện triển khai. |
| Phạm vi tăng hoặc duyệt chậm | Giảm thời gian xây dựng và kiểm thử trước 15/11. | Chốt tổng thể và đợt đầu ngày 30/10; thay đổi sau duyệt phải đánh giá lại công và mốc. |
| Thiếu năng lực phát triển/tích hợp/QA | Hai BA không thể thay đội thực hiện toàn module. | Chốt người và năng lực Angular, Java Spring Boot, Oracle/tích hợp, test dữ liệu và triển khai; tính công riêng. |
| Chưa rõ người dùng, quyền và tác nghiệp phần 2 | Có thể làm màn hình không dùng được hoặc mở dữ liệu sai phạm vi. | Xác nhận vai trò/phạm vi truy cập, quy trình và chủ thể xử lý trước khi đặc tả chi tiết KT. |

### Đề nghị ban giám đốc XVK quyết định

1. Cho phép khảo sát để chốt phương án hợp tác trọn module; xác định người chịu trách nhiệm làm việc với VNPT-IT.
2. Bố trí 2 BA ban đầu và khả năng hỗ trợ thêm theo tải thực tế; không cam kết một BA đủ toàn bộ công việc trong 5 ngày.
3. Chuẩn bị đầu mối kỹ thuật và QA để ước lượng phần đầu; xác nhận công BA hỗ trợ sau tuần khảo sát.
4. Duyệt định hướng DB01 cho đợt demo; toàn bộ use case và 5 dashboard vẫn được trình trong bản vẽ tổng thể.
5. Chỉ chốt cam kết 15/11 khi dữ liệu, môi trường, người thực hiện, phạm vi và tiêu chí bàn giao đã được xác nhận.

**Cơ sở nhận việc:** hướng tiếp cận có thể triển khai từng phần và phù hợp để bước vào khảo sát. Khả thi của từng chỉ tiêu/use case, số BA thực tế và cam kết tiến độ phải dựa trên bằng chứng ở tuần đầu. Báo cáo này cung cấp phương án nghiệp vụ cụ thể để ban giám đốc đánh giá và để VNPT-IT phản hồi, không thay biên bản phê duyệt phạm vi.
