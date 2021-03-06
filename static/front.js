public_key = 'Public Key not available';
private_key = 'Private Key not available';
balance = '0.0';
$('#show-blockchain, #show-transactions').hide();
$(document).ready(() => {

  $('#create-wallet').click(() => {
    $.post('/wallet', (data) => {
      $('#tip').text(data.message);
      public_key = data.public_key;
      private_key = data.private_key;
      balance = data.balance;
      $('#public-key').addClass('active');
      $('#private-key').removeClass('active');
      $('#wallet-id').text(public_key);
      $('#funds').text(balance);
    });
  });

  $('#load-wallet').click(() => {
    $.get('/wallet', (data) => {
      $('#tip').text(data.message);
      public_key = data.public_key;
      private_key = data.private_key;
      balance = data.balance;
      $('#public-key').addClass('active');
      $('#private-key').removeClass('active');
      $('#wallet-id').text(public_key);
      $('#funds').text(balance);
    });
  });

  $('#public-key').click(() => {
    $('#public-key').addClass('active');
    $('#private-key').removeClass('active');
    $('#wallet-id').text(public_key);
  });

  $('#private-key').click(() => {
    $('#private-key').addClass('active');
    $('#public-key').removeClass('active');
    $('#wallet-id').text(private_key);
  });

  $('#add-btn').click(() => {
    $('#add-btn').addClass('active');
    $('#blockchain-btn, #transactions-btn').removeClass('active');
    $('#transaction-card').show();
    $('#show-blockchain, #show-transactions').hide();
  });

  $('#blockchain-btn').click(() => {
    $.get('/chain', (data) => {
      $('#tip').text(data.message)
      $('#show-blockchain').html('')
      list = '<ul></ul>';
      data.blockchain.forEach((block, i) => {
        block_num = `<button class="long hide-toggle">Block ${i}</button>`;
        block_content_list = '<ul class="p-hide"></ul>';
        transaction_str = ``
        for(const transaction of block.transactions){
          transaction_str += `<hr><p><u>SENDER</u></p><p>${transaction.sender}</p>`
          transaction_str += `<p><u>RECIPIENT</u></p><p>${transaction.recipient}</p>`
          transaction_str += `<p><u>AMOUNT</u></p><p>${transaction.amount}</p>`
          transaction_str += `<p><u>TIME</u></p><p>${transaction.time}</p>`
          if(transaction.signature){
            transaction_str += `<p><u>SIGNATURE</u></p><p>${transaction.signature}</p>`
          }
        }
        block_content_list = $(block_content_list).append(`<li><p><strong>INDEX</strong></p><p>${block.index}</p></li>`);
        block_content_list = $(block_content_list).append(`<li><p><strong>PREVIOUS HASH</strong></p><p>${block.prev_hash}</p></li>`);
        block_content_list = $(block_content_list).append(`<li><p><strong>TRANSACTIONS</strong></p>${transaction_str}</li>`);
        block_content_list = $(block_content_list).append(`<li><p><strong>PROOF</strong></p><p>${block.proof}</p></li>`);
        $(block_content_list).hide();
        list_el = $('<li></li>').append(block_num, block_content_list)
        list = $(list).prepend(list_el);
      });
      $('#show-blockchain').append(list);
    });
    $('#blockchain-btn').addClass('active');
    $('#add-btn, #transactions-btn').removeClass('active');
    $('#show-blockchain').show();
    $('#transaction-card, #show-transactions').hide();
  });

  $('#transactions-btn').click(() => {
    $.get('/transactions', (data) => {
      $('#tip').text(data.message)
      $('#show-transactions').html('')
      list = '<ul></ul>';
      transaction_str = ``
      for(const transaction of data.transactions){
        transaction_str += `<p><u>SENDER</u></p><p>${transaction.sender}</p>`
        transaction_str += `<p><u>RECIPIENT</u></p><p>${transaction.recipient}</p>`
        transaction_str += `<p><u>AMOUNT</u></p><p>${transaction.amount}</p>`
        transaction_str += `<p><u>TIME</u></p><p>${transaction.time}</p>`
        if(transaction.signature){
          transaction_str += `<p><u>SIGNATURE</u></p><p>${transaction.signature}</p>`
        }
        transaction_str += `<hr>`
        list = $(list).prepend(`<li>${transaction_str}</li>`)
        transaction_str = ``
      }
        
      $('#show-transactions').append(list);
    });
    $('#transactions-btn').addClass('active');
    $('#add-btn, #blockchain-btn').removeClass('active');
    $('#show-transactions').show();
    $('#transaction-card, #show-blockchain').hide();
  });

  $('#content').on('click','.hide-toggle',(event)=>{
    $(event.target).siblings().toggle()
  })

  $('#mine').click(() => {
    $.post('/mine', (data) => {
      balance = data.balance;
      $('#funds').text(balance);
      $('#add-btn').trigger('click');
      $('#tip').text(data.message);
    });
  });

  $('#submit-btn').click(() => {
    $.post('/add-transaction', (data) => {
      $('#tip').text(data.message);
      balance = data.balance;
      $('#funds').text(balance);
    });
  });

});
