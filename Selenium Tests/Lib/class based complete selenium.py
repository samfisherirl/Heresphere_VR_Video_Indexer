def connect_to_webpage(self):
    url_target_sg = 'http://railway1.hinet.net/csearch.htm'
    url_target_gb = 'http://railway.hinet.net/ctkind2.htm'
    self.driver.delete_all_cookies()

    wait = WebDriverWait(self.driver, timeout=6)
    try:
        # Booking Single Ticket.
        if self.book_type == 1:
            self.driver.get
            wait.until(
                EC.presence_of_element_located(
                    (By.TAG_NAME, 'button')
                )
            )
        # Booking Go-Back Ticket.
        elif self.book_type == 2:
            self.driver.get
            wait.until(
                EC.presence_of_element_located(
                    (By.TAG_NAME, 'button')
                )
            )
    except:
        self.label_show_result.setText(
            '【連線逾時或是網路不穩定】\n' +
            '【請檢查網路環境以及是否為尖峰時段。】'
        )
