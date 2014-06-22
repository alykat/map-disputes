$(function() {
  this._disputesEl = this.querySelector('.disputes')

  $('#js-toggleUsIndia').click(function (e) {
    var isUsView = $('.map--aksai-chin').hasClass('us-view')
    if (isUsView) {
      $('.map--aksai-chin').removeClass('us-view')
    } else {
      $('.map--aksai-chin').addClass('us-view')
    }
    $('.map--aksai-chin img.top').toggleClass('transparent')
    isUsView = !isUsView

    $('.disputed-name .current-view')[0].innerHTML =  isUsView ? 'US view' : 'India view'
    e.target.innerText = isUsView ? "What does India see?" : "What does the US see?"
  })

  if (!this._disputesEl) return

  var disputeMapEls = this._disputesEl.querySelectorAll('.disputed-img-wrap')
  var claimantMapEls = this._disputesEl.querySelectorAll('.claimants-item-map')

  for (var i = 0; i < disputeMapEls.length; i++) {
    disputeMapEls[i].style.backgroundImage = "url(" + disputeMapEls[i].getAttribute('data-url') + ")"
  }

  for (i = 0; i < claimantMapEls.length; i++) {
    claimantMapEls[i].style.backgroundImage = "url(" + claimantMapEls[i].getAttribute('data-url') + ")"
  }
});
