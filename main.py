import sys
from time import sleep

import pygame

# from character import Character
from alien import Alien
from game_stats import GameStats
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
       
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height= self.screen.get_rect().height
        pygame.display.set_caption("Alien invasion")

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_active = True
        # self.character = Character(self)

    def _create_alien(self, current_x, current_y):
        new_alien = Alien(self)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        new_alien.rect.y = current_y
        self.aliens.add(new_alien)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x, current_y = alien_width, alien_height
        while current_y < ((self.settings.screen_height/2) - 3 * alien_height):
            while (current_x < (self.settings.screen_width - 2 * alien_width)):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

    def _check_events(self, ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # self.character.blitme()
        pygame.display.flip()

    def _check_bullet_alien_collisions(self):
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        #checking for collision in sprite groups
        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit() 
        self._check_aliens_bottom()

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(self.settings.frame_rate)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.alien_ship_speed *= -1

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()
        
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
