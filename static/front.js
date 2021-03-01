public_key = 'Public Key not available';
private_key = 'Private Key not available';
balance = '0.0';

$(document).ready(() => {
  $('#create-wallet').click(() => {
    $.post('/wallet', (data) => {
      $('#tip').text(data.message);
      public_key = data.public_key;
      private_key = data.private_key;
      balance = data.balance;
      $('#public-key').addClass('active')
      $('#private-key').removeClass('active')
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
      $('#public-key').addClass('active')
      $('#private-key').removeClass('active')
      $('#wallet-id').text(public_key);
      $('#funds').text(balance);
    });
  });
  $('#public-key').click(()=>{
    $('#public-key').addClass('active')
    $('#private-key').removeClass('active')
    $('#wallet-id').text(public_key);
  })
  $('#private-key').click(()=>{
    $('#private-key').addClass('active')
    $('#public-key').removeClass('active')
    $('#wallet-id').text(private_key);
  })
});
