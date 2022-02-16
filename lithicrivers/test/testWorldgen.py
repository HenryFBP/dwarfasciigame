import unittest
from pprint import pprint

from lithicrivers.game import World, Tiles
from lithicrivers.model import VectorN


class RenderStuff(unittest.TestCase):
    def testworldGenConsistent(self):
        daClouds = \
            [
                [
                    Tiles.Cloud(),
                    Tiles.Cloud(),
                    Tiles.Cloud(),
                ],
                [
                    Tiles.Cloud(),
                    Tiles.Cloud(),
                    Tiles.Cloud(),
                ],
                [
                    Tiles.Cloud(),
                    Tiles.Cloud(),
                    Tiles.Cloud(),
                ]
            ],

        for _ in range(0, 100):
            worldData = World.gen_random_world_data(
                VectorN(3, 3, 2),
                gf_kwargs={
                    'choices': [Tiles.Tree()],
                    'weights': [69]
                }
            )

            mockData = \
                [
                    [  # z
                        [  # y
                            Tiles.Tree(),  # x
                            Tiles.Tree(),
                            Tiles.Tree(),
                        ],
                        [
                            Tiles.Tree(),
                            Tiles.Tree(),
                            Tiles.Tree(),
                        ],
                        [
                            Tiles.Tree(),
                            Tiles.Tree(),
                            Tiles.Tree(),
                        ]
                    ],
                    *daClouds
                ]

            self.assertEqual(worldData, mockData)

    def testWorldGenRandomSpread(self):
        daSize = 20

        world_data = World.gen_random_world_data(
            radius=(VectorN(daSize, daSize, 2)),
            gf_kwargs={
                "choices": [Tiles.Tree(), Tiles.Dirt()],
                "weights": [50, 50]
            }
        )

        count_tiles = {}
        for pos, tile in world_data:
            # print(tile)
            if tile.tileid not in count_tiles:
                count_tiles[tile.tileid] = 0
            count_tiles[tile.tileid] += 1

        pprint(count_tiles)

        numDirt = count_tiles[Tiles.Dirt().tileid]
        numTree = count_tiles[Tiles.Tree().tileid]
        numCloud = count_tiles[Tiles.Cloud().tileid]

        self.assertAlmostEqual(
            numDirt / (daSize * daSize),
            numTree / (daSize * daSize), 1)

        self.assertEqual(
            numDirt + numTree,
            numCloud)
