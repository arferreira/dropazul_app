;(function($){
	'use strict';
	
	/* ==========================================================================
	   Preloader
	   ========================================================================== */
	$(window).on('load', function() { // makes sure the whole site is loaded 
		$('#status').fadeOut(); // will first fade out the loading animation 
		$('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website. 
		$('body').delay(350).css({'overflow':'visible'});
	})
	/* ==========================================================================

	========================================================================== */
	var $vdoPop = $('.video');
	if($vdoPop.length > 0){
		$vdoPop.magnificPopup({
			type: 'iframe',
			iframe: {
				markup: '<style>.mfp-iframe-holder .mfp-content {max-width: 900px;height:500px}</style>' +
				'<div class="mfp-iframe-scaler" >' +
				'<div class="mfp-close"></div>' +
				'<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
				'</div></div>'
			}
		});
	}


/* ==========================================================================
	Testimonial Carousel
	========================================================================== */
	
	var quoteCarousel = $('.quote')
	if(quoteCarousel.length > 0){
		quoteCarousel.owlCarousel({
			loop:true,
			autoplay:true,
			autoplayTimeout:2500,
			margin: 30,
			nav: false,
			dots:false,
			responsive:{
				320:{
					items:1,
					margin:10
				},
				767:{
					items:2,
					margin:15
				},
				991:{
					items:2
				},
				1199:{
					items:3
				}
			}
		})
	}

	/* ==========================================================================
    device Carousel
========================================================================== */
  
    var $appSlide = $('.app-slide')
    if($appSlide.length > 0){
        $appSlide.owlCarousel({
            loop:true,
            center:true,
            margin: 0,
            items:1,
            nav: false,
            dots:true,
            dotsContainer: '.dots'
        })
        $('.owl-dot').on('click', function() {
        	$(this).addClass('active').siblings().removeClass('active');
          $appSlide.trigger('to.owl.carousel', [$(this).index(), 300]);
        });    
    }

	/* ==========================================================================
		Wow
		========================================================================== */
		new WOW().init();
		
	/* ==========================================================================
	  Mailchimp Form
	  ========================================================================== */
	  $('.subscribe form').on('submit', function(e) {
	  	e.preventDefault();
	  	var postdata = $('.subscribe form').serialize();
	  	$.ajax({
	  		type: 'POST',
	  		url: 'assets/subscribe.php',
	  		data: postdata,
	  		dataType: 'json',
	  		success: function(json) {
	  			if(json.valid == 0) {
	  				$('.success-message').hide();
	  				$('.error-message').hide();
	  				$('.error-message').html(json.message);
	  				$('.error-message').fadeIn('fast', function(){
	  					$('.subscribe form').addClass('animated shake').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
	  						$(this).removeClass('animated shake');
	  					});
	  				});
	  			}
	  			else {
	  				$('.error-message').hide();
	  				$('.success-message').hide();
	  				$('.subscribe form').hide();
	  				$('.success-message').html(json.message);
	  				$('.success-message').fadeIn('fast', function(){
	  					$('.top-content').backstretch("resize");
	  				});
	  			}
	  		}
	  	});
	  });
	/* ==========================================================================
			Menu click scroll
			========================================================================== */

			var $navItem = $('.right-nav a[href*="#"], .demo a[href*="#"]');
			if($navItem.length > 0 ){
				$navItem.on('click', function (e) {
					$(document).off("scroll");
					if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
						|| location.hostname == this.hostname) {

						var target = $(this.hash),
			headerHeight = $(".navbar").height()-2; // Get fixed header height

			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');

			if (target.length) {
				$('html,body').animate({
					scrollTop: target.offset().top - headerHeight
				}, 1000);
				return false;
			}
		}
	});
			}

	/* ==========================================================================
			accordion
			========================================================================== */
			var $pnlCllpse = $('.panel-collapse');

			$pnlCllpse.on('show.bs.collapse', function () {
				$(this).siblings('.panel-heading').addClass('active');
			});

			$pnlCllpse.on('hide.bs.collapse', function () {
				$(this).siblings('.panel-heading').removeClass('active');
			});	
			
		})(jQuery); 
