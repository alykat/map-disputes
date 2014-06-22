$(function() {
  this._disputesEl = this.querySelector('.disputes')

  if (!this._disputesEl) return

  var disputeMapEls = this._disputesEl.querySelectorAll('.disputes-item-map')
  var claimantMapEls = this._disputesEl.querySelectorAll('.claimants-item-map')

  for (var i = 0; i < disputeMapEls.length; i++) {
    disputeMapEls[i].style.backgroundImage = "url(" + disputeMapEls[i].getAttribute('data-url') + ")"
  }

  for (i = 0; i < claimantMapEls.length; i++) {
    claimantMapEls[i].style.backgroundImage = "url(" + claimantMapEls[i].getAttribute('data-url') + ")"
  }
});
